"""RIFLEX storage: time series in ``<stem>.bin`` or ``<stem>.asc``, described by ``key_<stem>.txt``.

A port of SIMA's ``RIFLEXStorageImporter`` -- ``StorageMeta``, ``StorageFileReader``
and one ``*LookupData`` per key-file layout -- so the tree, names and units are
the ones SIMA's post processor shows.

A binary file is Fortran sequential unformatted, one record per time step:
``[int32 length][float32 time][float32 x N][int32 length]``. RIFLEX's key file
counts the record markers as columns, so binary data starts at column 3 and
ASCII, which has none, at column 2: in both, the 0-based index into a row is the
key column less one.

SIMA has no reader for ASCII storage; this one reads it with the binary file's
key-file layouts, which RIFLEX writes for both.

Not ported: the stress SIMA computed from element forces for run folders from
before sima/issue#940. RIFLEX's OUTMOD computes it since.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, ClassVar

import numpy as np

from .._build import add_signal, graft, set_attribute, set_type
from .._node import Container, Equidistant, Signal
from .._registry import register
from .._riflexres import DEFAULT, ElementRef, MapperError, RiflexMapper, read_mapper
from .._sources import Source, SourceError
from .._units import base_unit

TYPE_LINE = "line"
TYPE_SEGMENT = "segment"
TYPE_ELEMENT = "element"
TYPE_NODE = "node"
TYPE_SUPERNODE = "supernode"
TYPE_BODY = "body"
INDEX = "index"
TIME_UNIT = "s"

ENCODING = "latin-1"

#: Key-file kinds SIMA recognises by the file name rather than by its text.
_KINDS_BY_NAME = frozenset({"witurb", "blresp", "supportforce", "wavkin", "updkin"})

_TIME_SERIES_OF = "contains a time series of "

_FORTRAN = "FORTRAN specific data"

#: How many lines the old key-file layout has before its table, at least.
_HEADER_LINES = 14

#: RIFLEX storage, which is a result only beside its key file: turbulence boxes
#: (``wind_u.bin``), FEM ``*_eledat.asc`` and fibre files share the extensions.
SUFFIXES = frozenset({".bin", ".asc"})


def storage_key(path: Path) -> Path:
    """The key file describing a RIFLEX storage file: ``key_<stem>.txt`` beside it."""
    return path.parent / f"key_{path.stem}.txt"


@dataclass
class _Response:
    name: str
    #: The SI unit SIMA labels the signal with.
    unit: str
    #: 0-based index into a time step's row.
    column: int


@dataclass
class _Row:
    """One row of a key file: ``SMeta``."""

    owner: str
    segment: int = -1
    #: The element or node number.
    number: int = -1
    is_element: bool = True
    #: False for a supernode, whose signals sit on its own container.
    is_line: bool = True
    responses: list[_Response] = field(default_factory=list)
    #: Kind-specific: the support force's body, node and line; the turbine's name.
    extra: dict[str, str] = field(default_factory=dict)


# --------------------------------------------------------------------------
# the numbers
# --------------------------------------------------------------------------


class _Data:
    """The storage file's numbers, read whole on first use and kept."""

    def __init__(self, path: Path, columns: int):
        self.path = path
        self.binary = path.suffix.lower() == ".bin"
        #: Columns in a time step's row, markers included.
        self.columns = columns + (3 if self.binary else 1)
        self._matrix: np.ndarray | None = None
        if self.binary:
            self.size, first = self._binary_layout()
        else:
            self.size, first = self._ascii_layout()
        # StorageMeta.findTimestep: from the first two steps, and a missing
        # second step reads as zero, as SIMA's zero-filled buffer does.
        self.start = first[0] if first else 0.0
        self.delta = abs((first[1] if len(first) > 1 else 0.0) - self.start) if first else 0.0

    def _binary_layout(self) -> tuple[int, list[float]]:
        words, remainder = divmod(self.path.stat().st_size, 4)
        if remainder or words % self.columns:
            raise SourceError(
                f"{self.path.name} holds {words} values, not whole steps of the "
                f"{self.columns} columns its key file describes")
        head = np.fromfile(self.path, dtype="<i4", count=1)
        expected = 4 * (self.columns - 2)
        if head.size and head[0] != expected:
            raise SourceError(
                f"{self.path.name} has records of {head[0]} bytes, but its key file "
                f"describes {expected}")
        first = np.fromfile(self.path, dtype="<f4", count=min(words, 2 * self.columns))
        times = [float(first[i * self.columns + 1]) for i in range(len(first) // self.columns)]
        return words // self.columns, times

    def _ascii_layout(self) -> tuple[int, list[float]]:
        size = 0
        times: list[float] = []
        with self.path.open("rb") as file:
            for line in file:
                if not line.strip():
                    continue
                if size < 2:
                    times.append(float(line.split()[0]))
                size += 1
        return size, times

    def matrix(self) -> np.ndarray:
        """Every time step's row, record markers included."""
        if self._matrix is None:
            if self.binary:
                values = np.fromfile(self.path, dtype="<f4")
            else:
                values = np.loadtxt(self.path, dtype=np.float64, ndmin=2)
            if values.size != self.size * self.columns:
                raise SourceError(f"{self.path.name} changed since it was opened")
            self._matrix = values.reshape(self.size, self.columns)
        return self._matrix

    def column(self, index: int) -> np.ndarray:
        """One column widened to float64, as ``StorageSeries`` widens it."""
        return self.matrix()[:, index].astype(np.float64)


class _Values(Equidistant):
    """A signal's values, computed from the storage file when read."""

    def __init__(self, data: _Data, compute: Callable[[], np.ndarray]):
        super().__init__(data.size, data.start, data.delta)
        self._compute = compute

    def y(self) -> np.ndarray:
        values = self._compute()
        values.flags.writeable = False
        return values


# --------------------------------------------------------------------------
# key files
# --------------------------------------------------------------------------


def _kind_of(key: Path, lines: list[str]) -> str:
    """``StorageMeta.findType``: by name for a few, else by what the text says it holds."""
    stem = key.name.lower()
    if stem.endswith(".txt") and "_" in stem:
        by_name = stem[stem.rindex("_") + 1:-len(".txt")]
        if by_name in _KINDS_BY_NAME:
            return by_name
    for line in lines[:_HEADER_LINES]:
        if _TIME_SERIES_OF in line:
            return line.split(_TIME_SERIES_OF)[1].strip()
    return ""


def _description(tokens: list[str]) -> str:
    """The rest of a row, one space between words, as StringTokenizer rejoins it."""
    return " ".join(tokens)


def _uncommented(lines: list[str]) -> list[list[str]]:
    return [line.split() for line in lines if line.strip() and not line.startswith("'")]


class _Layout:
    """One key-file layout and how its rows become a tree: a ``StorageLookupData``."""

    #: Response names by index, for the layouts that do not spell them out.
    names: ClassVar[tuple[str, ...]] = ()
    units: ClassVar[tuple[str, ...]] = ()
    is_element: ClassVar[bool] = True

    def __init__(self, binary: bool):
        #: The key column holding time; data follows it.
        self.time_column = 2 if binary else 1

    def rows(self, lines: list[str]) -> list[_Row]:
        """``StorageLookupData.findColumns``: the block table after the dashes."""
        rows = []
        index = _HEADER_LINES - 1
        while index < len(lines) and "-----------------" not in lines[index]:
            index += 1
        for line in lines[index + 1:]:
            if not line:
                break
            rows.append(self.row(line.split()))
        return rows

    def row(self, tokens: list[str]) -> _Row:
        """Line, segment, element or node, response count, first column: ``parseMeta``."""
        first = int(tokens[4]) - 1
        count = int(tokens[3])
        return _Row(
            owner=tokens[0], segment=int(tokens[1]), number=int(tokens[2]),
            is_element=self.is_element,
            responses=[_Response(self.name(i), self.unit(i), first + i) for i in range(count)],
        )

    def name(self, index: int) -> str:
        """The response's name, which the old layout leaves to the reader."""
        if index >= len(self.names):
            raise ValueError(f"unknown response {index}")
        return self.names[index]

    def unit(self, index: int) -> str:
        """The response's SI unit; one entry stands for all."""
        return self.units[index] if len(self.units) > 1 else self.units[0]

    def build(self, rows: list[_Row], data: _Data, context: _Context, into: Container) -> None:
        """``StorageLookupData.importStorage``: one container per line, then segment and element or node."""
        tree = context.tree
        for row in rows:
            if not row.is_line:
                owner = tree.child(into, context.long_id(row.owner), TYPE_SUPERNODE)
                for response in row.responses:
                    add_signal(owner, context.signal(response, data))
                continue
            line = tree.child(into, context.long_id(row.owner), TYPE_LINE)
            if row.segment == -1:
                for response in row.responses:
                    add_signal(line, context.signal(response, data))
                continue
            segment = tree.child(line, f"segment_{row.segment}", TYPE_SEGMENT)
            set_attribute(segment, INDEX, str(row.segment))
            prefix = "element" if row.is_element else "node"
            owner = tree.child(segment, f"{prefix}_{row.number}",
                               TYPE_ELEMENT if row.is_element else TYPE_NODE)
            set_attribute(owner, INDEX, str(row.number))
            self.add(row, owner, data, context)

    def add(self, row: _Row, owner: Container, data: _Data, context: _Context) -> None:
        """``ElementMeta.addMeta`` / ``NodeMeta.addMeta``."""
        prefix = "element" if row.is_element else "node"
        for response in row.responses:
            add_signal(owner, context.signal(response, data, **{prefix: f"{prefix}_{row.number}"}))


class _Curvature(_Layout):
    names = ("Curvature about local y-axis, end 1", "Curvature about local y-axis, end 2",
             "Curvature about local z-axis, end 1", "Curvature about local z-axis, end 2")
    units = ("1/m",)


class _Displacements(_Layout):
    names = ("Displacement in x - direction", "Displacement in y - direction",
             "Displacement in z - direction")
    units = ("m",)
    is_element = False


class _Forces(_Layout):
    names = ("Axial force", "Torsional moment",
             "Mom. about local y-axis, end 1", "Mom. about local y-axis, end 2",
             "Mom. about local z-axis, end 1", "Mom. about local z-axis, end 2",
             "Shear force in local y-direction, end 1", "Shear force in local y-direction, end 2",
             "Shear force in local z-direction, end 1", "Shear force in local z-direction, end 2")
    units = ("N", "N*m", "N*m", "N*m", "N*m", "N*m", "N", "N", "N", "N")


class _SumForces(_Layout):
    names = ("Axial sum force",)
    units = ("N",)


class _ContactForces(_Layout):
    """Pipe-in-pipe contact; each name says which of the node's contacts it is (sima/issue#944)."""

    names = ("Contact force in local x-direction", "Contact force in local y-direction",
             "Contact force in local z-direction", "Moment about local x-axis",
             "Contact force in global x-direction", "Contact force in global y-direction",
             "Contact force in global z-direction", "Moment about global x-axis",
             "Moment about global y-axis", "Moment about global z-axis")
    units = ("N", "N", "N", "N*m", "N", "N", "N", "N*m", "N*m", "N*m")
    is_element = False

    def __init__(self, binary: bool):
        super().__init__(binary)
        self._per_node: dict[tuple[str, str, str], int] = {}

    def row(self, tokens: list[str]) -> _Row:
        row = super().row(tokens)
        node = (row.owner, str(row.segment), str(row.number))
        self._per_node[node] = self._per_node.get(node, 0) + 1
        # line, segment, node, responses, first column, "-", last column, contact
        contact = tokens[7] if len(tokens) > 7 else f"Contact {self._per_node[node]}"
        for response in row.responses:
            response.name = f"{response.name} - {contact}"
        return row


class _Transformation(_Layout):
    """``element-tracon``: never shown raw, only as the angles and matrix derived from it."""

    names = tuple(f"TRACON {i + 1}" for i in range(9))
    units = ("-",)

    def add(self, row: _Row, owner: Container, data: _Data, context: _Context) -> None:
        ref = (row.owner, row.segment, row.number)
        for other in context.mapper.relative_angles.get(ref, ()):
            add_signal(owner, self._relative_angle(row, other, data, context))
        for angle in context.mapper.element_angles:
            if angle.element == ref:
                add_signal(owner, _signal(
                    f"Angle with {angle.axis} axis, projected in {angle.plane} plane", "deg",
                    _Values(data, _element_angle(row, angle.plane, angle.axis, data))))
        if context.mapper.read_matrices:
            matrix = graft(owner, Container("Transformation matrix from local to global"))
            for r in range(3):
                for c in range(3):
                    add_signal(matrix, _signal(f"T{r + 1}{c + 1}", "-",
                                               _Values(data, _tracon(row, r, c, data))))

    def _relative_angle(self, row: _Row, other: ElementRef, data: _Data,
                        context: _Context) -> Signal:
        line, segment, element = other
        match = next((r for r in context.rows if (r.owner, r.segment, r.number) == other), None)
        if match is None:
            raise ValueError(f"Was not able to find storage of line {line} segment {segment} "
                             f"element {element}")

        def compute() -> np.ndarray:
            dot = sum(_tracon(row, i, 0, data)() * _tracon(match, i, 0, data)() for i in range(3))
            return np.degrees(np.arccos(np.clip(dot, -1.0, 1.0)))

        return _signal(f"Relative angle to {context.long_id(line)}, segment {segment}, "
                       f"element {element}", "deg", _Values(data, compute))


def _tracon(row: _Row, r: int, c: int, data: _Data) -> Callable[[], np.ndarray]:
    """The stored matrix entry (r, c), unscaled: ``TransformationMatrixStorage.getValues``."""
    return lambda: data.column(row.responses[r * 3 + c].column)


#: Plane and axis to (y row, y col, x row, x col): ``ElementAngleStorageSeries.getIndices``.
_ANGLE_INDICES: dict[tuple[str, str], tuple[int, int, int, int]] = {
    ("XY", "X"): (1, 0, 0, 0), ("XY", "Y"): (0, 0, 1, 0),
    ("XZ", "X"): (2, 0, 0, 0), ("XZ", "Z"): (0, 0, 2, 0),
    ("YZ", "Y"): (2, 0, 1, 0), ("YZ", "Z"): (1, 0, 2, 0),
}


def _element_angle(row: _Row, plane: str, axis: str, data: _Data) -> Callable[[], np.ndarray]:
    indices = _ANGLE_INDICES.get((plane, axis))
    if indices is None:
        raise ValueError(f"Unsupported element angle: {axis} axis in {plane} plane")
    y_row, y_col, x_row, x_col = indices
    return lambda: np.degrees(np.arctan2(_tracon(row, y_row, y_col, data)(),
                                         _tracon(row, x_row, x_col, data)()))


class _General(_Layout):
    """Self-describing element storage such as ``hydloa``: ``GeneralElementStorageLookupData``."""

    _COLUMNS: ClassVar[dict[str, str]] = {
        "LINE": "line", "LSEG": "segment", "LELM": "element", "ELEND": "end",
        "UNIT": "unit", "DESC": "name"}

    def rows(self, lines: list[str]) -> list[_Row]:
        rows = []
        layout: list[str] | None = None
        for tokens in _uncommented(lines):
            if len(tokens) <= 3:
                continue
            column = int(tokens[0])
            if column == 0:
                unknown = [token for token in tokens[1:] if token not in self._COLUMNS]
                if unknown:
                    raise ValueError(f"Unknown column id: {unknown[0]}")
                layout = [self._COLUMNS[token] for token in tokens[1:]]
            elif column > self.time_column:
                fields = self._guided(layout, tokens[1:]) if layout else self._default(tokens[1:])
                if fields is None:
                    continue
                end = int(fields.get("end", -1))
                name = fields["name"] + (f", end {end}" if end > 0 else "")
                rows.append(_Row(
                    owner=fields["line"], segment=int(fields["segment"]),
                    number=int(fields["element"]),
                    responses=[_Response(name, _general_unit(fields["unit"]), column - 1)]))
        return rows

    @staticmethod
    def _guided(layout: list[str], tokens: list[str]) -> dict[str, str] | None:
        fields: dict[str, str] = {}
        for i, key in enumerate(layout):
            if key == "name":
                fields[key] = _description(tokens[i:])
                break
            fields[key] = tokens[i]
            if i == 0 and fields[key] == "-":
                return None
        return fields

    @staticmethod
    def _default(tokens: list[str]) -> dict[str, str] | None:
        if tokens[0] == "-":
            return None
        fields = {"line": tokens[0], "segment": tokens[1], "element": tokens[2]}
        # The token after the element is the end only if it is a number; either way the unit follows it.
        if tokens[3].lstrip("-").isdigit():
            fields["end"] = tokens[3]
        fields["unit"] = tokens[4]
        fields["name"] = _description(tokens[5:])
        return fields


#: Labels the general and blade layouts map by hand, before trying the registry.
_GENERAL_UNITS: dict[str, str] = {
    "deg": "deg", "m/s": "m/s", "kN": "N", "N": "N", "kN/m": "N/m", "N/m": "N/m",
    "kN*m/m": "N*m/m", "N*m/m": "N*m/m", "-": "-"}


def _general_unit(label: str) -> str:
    return _GENERAL_UNITS.get(label) or base_unit(label) or "?"


class _SeaFloorContact(_Layout):
    """``botres``: ``SeaFloorContactLookupData``. A key file without comment lines is not read, as in SIMA."""

    _UNITS: ClassVar[dict[str, str]] = {
        "L": "m", "F": "N", "FL": "N*m", "F/L": "N/m", "F/L**2": "N/m^2",
        "FL/deg": "N*m/deg", "FL/(L*deg)": "N*m/m*deg", "FL/L": "N*m/m", "deg": "deg"}

    def rows(self, lines: list[str]) -> list[_Row]:
        if not lines or not lines[0].startswith("'"):
            return []
        rows = []
        for tokens in _uncommented(lines[1:]):
            column = int(tokens[0])
            if column <= self.time_column or tokens[2] == "-":
                continue
            end = _int_or_none(tokens[5])
            if tokens[6] not in self._UNITS:
                raise ValueError(f"unknown unit {tokens[6]}")
            name = _description(tokens[7:]) + (f" - End {end}" if end >= 0 else "")
            rows.append(_Row(owner=tokens[2], segment=_int_or_none(tokens[3]),
                             number=_int_or_none(tokens[4]),
                             responses=[_Response(name, self._UNITS[tokens[6]], column - 1)]))
        return rows


def _int_or_none(token: str) -> int:
    return -1 if token == "-" else int(token)


class _WaveKinematics(_Layout):
    """``wavkin`` and ``updkin``. A key file without comment lines is not read, as in SIMA."""

    is_element = False

    def rows(self, lines: list[str]) -> list[_Row]:
        if not lines or not lines[0].startswith("'"):
            return []
        rows = []
        for tokens in _uncommented(lines[1:]):
            column = int(tokens[0])
            if column <= self.time_column or tokens[1] == "-":
                continue
            is_line = tokens[1] == "LINE"
            segment, node = (int(tokens[3]), int(tokens[4])) if is_line else (-1, -1)
            int(tokens[5])  # FEM node
            for coordinate in tokens[6:9]:
                float(coordinate)
            unit = base_unit(tokens[9]) or "?"
            rows.append(_Row(owner=tokens[2], segment=segment, number=node, is_element=False,
                             is_line=is_line,
                             responses=[_Response(_description(tokens[10:]), unit, column - 1)]))
        return rows


class _WindTurbine(_Layout):
    """``witurb``: one container per turbine, signals directly on it."""

    _UNITS: ClassVar[dict[str, str]] = {
        "s": "s", "deg/s": "deg/s", "rpm": "rpm", "deg": "deg", "kNm": "N*m", "Nm": "N*m",
        "W": "W", "kW": "W", "m/s": "m/s", "N": "N", "kN": "N", "m": "m"}

    def rows(self, lines: list[str]) -> list[_Row]:
        rows = []
        several = False
        for line in lines:
            if not line or line.startswith("'") or _FORTRAN in line:
                continue
            tokens = line.split()
            if len(tokens) <= 3:
                continue
            column = int(tokens[0])
            if column == self.time_column:
                several = len(tokens) == 5
            if column <= self.time_column:
                continue
            turbine = "Wind Turbine"
            if several:
                turbine, tokens = tokens[1], tokens[1:]
            if tokens[2] not in self._UNITS:
                raise ValueError(f"unknown unit {tokens[2]}")
            rows.append(_Row(owner=turbine, responses=[
                _Response(_description(tokens[3:]), self._UNITS[tokens[2]], column - 1)]))
        return rows

    def build(self, rows: list[_Row], data: _Data, context: _Context, into: Container) -> None:
        for row in rows:
            turbine = context.tree.child(into, context.long_id(row.owner))
            for response in row.responses:
                signal = add_signal(turbine, context.signal(response, data))
                if response.name == "Rotor speed":
                    add_signal(turbine, _signal(f"{response.name} (rpm)", "rpm",
                                                _Values(data, lambda s=signal: s.y / 6.0)))


class _Blade(_Layout):
    """``blresp``: ``WindTurbineBladeLookupData``."""

    def rows(self, lines: list[str]) -> list[_Row]:
        rows = []
        for line in lines:
            if not line or line.startswith("'") or _FORTRAN in line:
                continue
            tokens = line.split()
            if len(tokens) <= 3 or int(tokens[0]) <= self.time_column:
                continue
            rows.append(_Row(owner=tokens[2], segment=int(tokens[3]), number=int(tokens[4]),
                             responses=[_Response(_description(tokens[6:]),
                                                  _general_unit(tokens[5]), int(tokens[0]) - 1)]))
        return rows


class _SupportForce(_Layout):
    """``supportforce``: body, ``Slender system forces``, node, and a line only beside a resultant."""

    _UNITS: ClassVar[dict[str, str]] = {
        "deg": "deg", "m/s": "m/s", "kN": "N", "kN/m": "N/m", "kNm": "N*m", "-": "-"}

    def rows(self, lines: list[str]) -> list[_Row]:
        rows = []
        for line in lines:
            if not line or line.startswith("'") or _FORTRAN in line:
                continue
            tokens = line.split()
            if len(tokens) <= 4:
                continue
            if tokens[2] not in self._UNITS:
                raise ValueError(f"unknown unit {tokens[2]}")
            node = f"Global Node {int(tokens[4])}" if tokens[6] == "_" else tokens[6]
            rows.append(_Row(owner=tokens[7], extra={"body": tokens[3], "node": node},
                             responses=[_Response(_description(tokens[8:]),
                                                  self._UNITS[tokens[2]], int(tokens[0]) - 1)]))
        return rows

    def build(self, rows: list[_Row], data: _Data, context: _Context, into: Container) -> None:
        resultant = {row.extra["node"] for row in rows if row.owner == "_ALL_"}
        tree = context.tree
        for row in rows:
            body = context.body_name(row.extra["body"])
            owner = tree.child(into, body)
            set_type(owner, TYPE_BODY)
            set_attribute(owner, TYPE_BODY, body)
            forces = tree.child(owner, "Slender system forces")
            owner = tree.child(forces, context.long_id(row.extra["node"]))
            if row.extra["node"] in resultant and row.owner != "_ALL_":
                owner = tree.child(owner, context.long_id(row.owner))
            for response in row.responses:
                add_signal(owner, context.signal(response, data))


#: ``StorageMeta.createLookupData``: anything unnamed here is general element storage.
_LAYOUTS: dict[str, type[_Layout]] = {
    "element-curvature": _Curvature,
    "nodal-displacements": _Displacements,
    "element-forces": _Forces,
    "contact-forces": _ContactForces,
    "sum-element-forces": _SumForces,
    "wave-kinematics": _WaveKinematics,
    "wavkin": _WaveKinematics,
    "updkin": _WaveKinematics,
    "element-tracon": _Transformation,
    "seafloor-contact": _SeaFloorContact,
    "witurb": _WindTurbine,
    "blresp": _Blade,
    "supportforce": _SupportForce,
}


# --------------------------------------------------------------------------
# the tree
# --------------------------------------------------------------------------


class _Tree:  # pylint: disable=too-few-public-methods
    """Children by name, as SIMA's maps keep them: a segment can hold thousands of nodes.

    Exact only because the reader fills a fresh container, so every child is one made here.
    """

    def __init__(self):
        self._made: dict[tuple[int, str, str | None], Container] = {}

    def child(self, parent: Container, name: str, kind: str | None = None) -> Container:
        """``getOrCreateChild``, or with a type ``StorageLookupData.findOrCreate``."""
        key = (id(parent), name, kind)
        child = self._made.get(key)
        if child is None:
            child = self._made[key] = graft(parent, Container(name, type=kind))
        return child


@dataclass
class _Context:
    source: Source
    mapper: RiflexMapper
    rows: list[_Row]
    tree: _Tree = field(default_factory=_Tree)

    def long_id(self, short: str) -> str:
        """The model name for a short id, or the id itself: ``getLongID``."""
        return self.source.context.resolve_id(short)

    def body_name(self, body: str) -> str:
        """A support vessel is numbered; anything else is a body's id."""
        if body.isdigit():
            vessels = self.mapper.support_vessels
            number = int(body)
            # SIMA fails the file without riflexres.inp to name the vessel; the number still says which.
            return vessels[number - 1] if 0 < number <= len(vessels) else body
        return self.long_id(body)

    def signal(self, response: _Response, data: _Data, **attributes: str) -> Signal:
        """A stored response, in SI: ``StorageSeries`` divides by the unit RIFLEX wrote in."""
        if response.column >= data.columns:
            raise ValueError(f"{response.name!r} is in column {response.column + 1}, "
                             f"past the {data.columns} the file has")
        factor = self.mapper.unit_factor(response.unit)
        return _signal(response.name, response.unit,
                       _Values(data, lambda: data.column(response.column) / factor), **attributes)


def _signal(name: str, unit: str, values: _Values, **attributes: str) -> Signal:
    return Signal(name, values, unit=unit, xunit=TIME_UNIT, **attributes)


@register
class RIFLEXStorageReader:  # pylint: disable=too-few-public-methods
    """Binary and ASCII storage, each beside its key file."""

    types = frozenset({"bin", "asc"})

    def read(self, source: Source, into: Container) -> None:
        """Fill ``into`` from the storage file, as its key file describes it."""
        key = storage_key(source.path)
        if not key.is_file():
            raise SourceError(f"RIFLEX storage key file {key.name} does not exist")
        lines = [line.rstrip("\r\n") for line in key.read_text(encoding=ENCODING).splitlines()]
        try:
            mapper = read_mapper(source.path.parent) or DEFAULT
        except MapperError as exc:
            raise SourceError(str(exc)) from exc
        binary = source.path.suffix.lower() == ".bin"
        layout = _LAYOUTS.get(_kind_of(key, lines), _General)(binary)
        rows = layout.rows(lines)
        data = _Data(source.path, sum(len(row.responses) for row in rows))
        layout.build(rows, data, _Context(source, mapper, rows), into)
