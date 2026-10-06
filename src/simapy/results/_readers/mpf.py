"""RIFLEX MatrixPlot files.

A port of SIMA's MatrixPlot import, keeping two passes apart rather than
parsing straight into arrays:

* the **structure pass** reads the ``MATRIX``/``TITLE``/``LEGENDS`` headers and
  notes where each block of numbers starts and how many rows it has;
* the **value pass** runs only when a signal's ``.x`` or ``.y`` is touched, and
  parses that one block.

So ``len()``, ``unit``, ``xunit`` and navigation never parse a number. Unlike
HDF5, a text format cannot slice from disk, so a matrix is parsed whole and
cached the first time any of its signals is read.

Files are read as bytes and decoded per line: the offsets recorded by the
structure pass have to be real byte positions, and Python's text-mode ``tell()``
returns an opaque cookie that cannot be arithmetic on.

Not ported: the post-transforms that reshape eigenvalue and outmod trees after
import.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import BinaryIO, ClassVar

import numpy as np

from .._build import (
    add_signal,
    clear_signals,
    get_or_create_child,
    graft,
    set_attribute,
    set_type,
)
from .._node import Container, ErrorSignal, Signal
from .._registry import register
from .._sources import FolderContext, Source, SourceError
from .._units import guard_unscaled, map_unit

#: The node type given to a line.
TYPE_LINE = "line"

#: The attribute naming a signal's line.
LINE_NAME = "line"

#: Matrices belonging to no line.
NO_LINE_ID = "None"

#: Marks a signal whose y axis is logarithmic.
STYLE_YAXIS_LOG = "yaxis.log"

ENCODING = "latin-1"

_COMMAND_WIDTH = 9
_VALUE_OFFSET = 10

#: Where a VALUES block ends.
_BLOCK_END = (b"MATRIX", b"END", b"HEADING")

_LEGEND = re.compile(r"'([^']*)'")


def is_static(filename: str) -> bool:
    """Whether a file is STAMOD's, which writes one matrix per load step."""
    return "stamod" in filename.lower()


# --------------------------------------------------------------------------
# value pass
# --------------------------------------------------------------------------


@dataclass
class _Block:  # pylint: disable=too-many-instance-attributes
    """Where one matrix's numbers live, and the numbers once parsed."""

    path: Path
    offset: int
    rows: int
    columns: int
    x_column: int = 0
    x_factor: float = 1.0
    y_factor: float = 1.0
    _parsed: np.ndarray | None = field(default=None, repr=False)

    def columns_array(self) -> np.ndarray:
        """``(columns, rows)`` float64 in base units, read-only. Parsed once, then cached.

        Read-only so every signal of the matrix can be handed a row without a copy.
        """
        if self._parsed is None:
            parsed = self._parse()
            parsed.flags.writeable = False
            self._parsed = parsed
        return self._parsed

    def _parse(self) -> np.ndarray:
        values = np.full((self.rows, self.columns), np.nan, dtype=np.float64)
        with self.path.open("rb") as handle:
            handle.seek(self.offset)
            row = 0
            while row < self.rows:
                start = handle.tell()
                line = handle.readline()
                if not line or line.startswith(_BLOCK_END):
                    raise SourceError(
                        f"{self.path.name}: matrix at offset {self.offset} ended after "
                        f"{row} of {self.rows} rows"
                    )
                tokens = line[_VALUE_OFFSET:].decode(ENCODING).split()
                if not tokens:
                    continue
                # Filling stops when a row runs short; the rest stays NaN.
                width = min(self.columns, len(tokens))
                try:
                    values[row, :width] = np.array(tokens[:width], dtype=np.float64)
                except ValueError as error:
                    raise SourceError(
                        f"{self.path.name}, line {_line_number(self.path, start)}: {error}"
                    ) from error
                row += 1

        factors = np.full((self.columns, 1), self.y_factor)
        factors[self.x_column] = self.x_factor
        return values.T / factors


def _line_number(path: Path, offset: int) -> int:
    with path.open("rb") as handle:
        return handle.read(offset).count(b"\n") + 1


class _MatrixValues:
    """One y-series of one matrix. Implements ``node.Values``; the block caches."""

    # pylint: disable=missing-function-docstring  # the Values protocol documents these

    def __init__(self, block: _Block, y_column: int):
        self._block = block
        self._y_column = y_column

    @property
    def size(self) -> int:
        return self._block.rows

    def x(self) -> np.ndarray:
        return self._block.columns_array()[self._block.x_column]

    def y(self) -> np.ndarray:
        return self._block.columns_array()[self._y_column]


# --------------------------------------------------------------------------
# structure pass
# --------------------------------------------------------------------------


@dataclass
class _Matrix:  # pylint: disable=too-many-instance-attributes
    """A parsed MATRIX header. ``PlotMatrix`` minus the values."""

    identifier: str = ""
    title: str = ""
    subtitle: str = ""
    x_label: str = ""
    y_label: str = ""
    x_unit: str = ""
    y_unit: str = "?"
    legends: tuple[str, ...] = ()
    x_column: int = 0
    y_columns: tuple[int, ...] = ()
    y_log: bool = False
    block: _Block | None = None
    #: Set when the file ends inside this matrix's headers.
    error: SourceError | None = None

    def set_legends(self, legends: tuple[str, ...]) -> None:
        """Legend 0 is the x-axis; the rest become signals."""
        self.legends = legends
        self.x_column = 0
        self.y_columns = tuple(range(1, len(legends)))

    def switch_xy(self) -> None:
        """``PlotMatrix.switchXY``: two series, swapped, units along with them."""
        if len(self.legends) != 2:
            raise SourceError(
                f"A matrix with option SWITCHXY should have two series. "
                f"{self.title!r} has {len(self.legends)}."
            )
        self.x_column, self.y_columns = 1, (0,)
        self.x_unit, self.y_unit = self.y_unit, self.x_unit


def _parse_headers(path: Path, context: FolderContext) -> list[_Matrix]:
    """Read every MATRIX block's headers. Does not parse a single value.

    A file ending inside a matrix's headers keeps the matrices before it, and the
    truncated one carries its error. With nothing before it, the file fails.
    """
    matrices: list[_Matrix] = []
    with path.open("rb") as handle:
        line = handle.readline()
        while line:
            if line.startswith(b"MATRIX"):
                matrix, line = _parse_matrix(handle, line, path, context)
                if matrix.error is not None and not matrices:
                    raise matrix.error
                matrices.append(matrix)
            else:
                line = handle.readline()
    return matrices


def _parse_matrix(
    handle: BinaryIO, id_line: bytes, path: Path, context: FolderContext
) -> tuple[_Matrix, bytes]:
    """Parse one MATRIX block's headers. Returns it and the line that ended it."""
    identifier = id_line.decode(ENCODING)[_VALUE_OFFSET:].strip()
    matrix = _Matrix(identifier=context.resolve_names(identifier))

    while True:
        position = handle.tell()
        line = handle.readline()
        if not line:
            matrix.error = SourceError(f"{path.name}: truncated matrix {matrix.identifier!r}")
            return matrix, b""

        text = line.decode(ENCODING)
        command = text[:_COMMAND_WIDTH].strip()
        value = text[_VALUE_OFFSET:].strip()

        if command == "TITLE":
            matrix.title = context.resolve_names(value)
        elif command == "SUBTITLE":
            matrix.subtitle = context.resolve_names(value)
        elif command == "XLABEL":
            matrix.x_label, matrix.x_unit = _x_label(value, context)
        elif command == "YLABEL":
            matrix.y_label, matrix.y_unit = _y_label(value, context, matrix.y_unit)
        elif command == "LEGENDS":
            matrix.set_legends(tuple(_LEGEND.findall(context.resolve_names(value))))
        elif command == "OPTIONS":
            option = value.strip().strip("'").split("'")[0]
            if option == "SWITCHXY":
                matrix.switch_xy()
            elif option == "YLOG":
                matrix.y_log = True
        elif command == "VALUES":
            return _scan_values(handle, matrix, path, position)


def _scan_values(
    handle: BinaryIO, matrix: _Matrix, path: Path, offset: int
) -> tuple[_Matrix, bytes]:
    """Count the rows of a VALUES block without converting them."""
    rows = 1
    while True:
        line = handle.readline()
        if not line:
            terminator = b""
            break
        if line.startswith(_BLOCK_END):
            terminator = line
            break
        if line.strip():
            rows += 1

    matrix.block = _Block(
        path=path,
        offset=offset,
        rows=rows,
        columns=len(matrix.legends),
        x_column=matrix.x_column,
        x_factor=map_unit(matrix.x_unit)[1],
        y_factor=map_unit(matrix.y_unit)[1],
    )
    return matrix, terminator


def _split_label(value: str, context: FolderContext) -> tuple[str, str] | None:
    """``"Line length [m]"`` -> ``("Line length", "m")``, or None with no ``[``.

    The closing bracket is optional, since a label can be cut short.
    """
    start = value.rfind("[")
    if start == -1:
        return None
    unit = value[start + 1 :].strip()
    if unit.endswith("]"):
        unit = unit[:-1].strip()
    return context.resolve_names(value[:start].strip()), unit


def _x_label(value: str, context: FolderContext) -> tuple[str, str]:
    """As :func:`_split_label`; no bracket -> unit ``""``."""
    split = _split_label(value, context)
    return split if split is not None else (context.resolve_names(value.strip()), "")


def _y_label(value: str, context: FolderContext, current_unit: str) -> tuple[str, str]:
    """As :func:`_split_label`; no bracket blanks the label and keeps the unit."""
    split = _split_label(value, context)
    return split if split is not None else ("", current_unit)


# --------------------------------------------------------------------------
# tree building
# --------------------------------------------------------------------------


def _line_id_in(identifier: str) -> str | None:
    """The line id a matrix identifier names, if any."""
    index = identifier.find(", line")
    if index == -1:
        return None
    rest = identifier[index + 7 :].strip()
    space = rest.find(" ")
    return rest[:space] if space > -1 else rest


def _reshape_title(title: str) -> str:
    """``"Static forces, line RiserLine"`` -> ``"Static forces"``."""
    index = title.find(", line ")
    return title[:index].strip() if index > 0 else title


def _sort_on_line(
    matrices: list[_Matrix], context: FolderContext
) -> dict[str, list[_Matrix]]:
    """Group matrices by the line their identifier names, insertion-ordered."""
    grouped: dict[str, list[_Matrix]] = {}
    for matrix in matrices:
        line_id = _line_id_in(matrix.identifier)
        if line_id is None:
            line_id = NO_LINE_ID
        else:
            # The identifier already went through resolve_names, so this only
            # catches ids that appear nowhere in the text SIMA rewrites.
            line_id = context.names.get(line_id, line_id)
        grouped.setdefault(line_id, []).append(matrix)
    return grouped


@register
class MpfReader:  # pylint: disable=too-few-public-methods
    """Builds the tree a MatrixPlot file describes."""

    types: ClassVar[frozenset[str]] = frozenset({"mpf"})

    def read(self, source: Source, into: Container) -> None:
        """Read one mpf into a fresh container. See ``Reader.read``."""
        static = is_static(source.file)
        matrices = _parse_headers(source.path, source.context)

        for line_id, group in _sort_on_line(matrices, source.context).items():
            if line_id == NO_LINE_ID:
                parent = into
            else:
                parent = get_or_create_child(into, line_id)
                set_type(parent, TYPE_LINE)
            for matrix in group:
                self._add_matrix(parent, matrix, line_id, static)

    def _add_matrix(
        self, parent: Container, matrix: _Matrix, line_id: str, static: bool
    ) -> None:
        title = _reshape_title(matrix.title)
        name = f"{title} - {matrix.subtitle}" if title.startswith("Eigenvector") else title

        if matrix.error is not None:
            add_signal(parent, ErrorSignal(name or matrix.identifier, matrix.error))
            return

        if static:
            # STAMOD writes one matrix per load step. The last step wins, so the
            # container is reused and the earlier step's signals dropped.
            child = get_or_create_child(parent, name)
            clear_signals(child)
        else:
            child = graft(parent, Container(name))

        self._add_series(child, matrix, line_id)

    def _add_series(self, child: Container, matrix: _Matrix, line_id: str) -> None:
        if matrix.block is None or not matrix.y_columns:
            return
        x_unit = map_unit(matrix.x_unit)[0]
        y_unit = map_unit(matrix.y_unit)[0]

        for column in matrix.y_columns:
            guarded, marks = guard_unscaled(
                _MatrixValues(matrix.block, column),
                f"{child.path}/{matrix.legends[column]}",
                matrix.y_unit, matrix.x_unit,
            )
            signal = Signal(
                name=matrix.legends[column],
                values=guarded,
                unit=y_unit,
                xunit=x_unit,
                **marks,
            )
            if matrix.y_log:
                set_attribute(signal, STYLE_YAXIS_LOG, "true")
            if line_id != NO_LINE_ID:
                set_attribute(signal, LINE_NAME, line_id)
            add_signal(child, signal)
