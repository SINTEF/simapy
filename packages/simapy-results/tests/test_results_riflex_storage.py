"""RIFLEX binary and ASCII storage, checked against the same run's HDF5 storage.

Each folder under ``data/riflex_storage`` is one RIFLEX run of one of srv's own test models,
stored three times: as binary (``bin/``), as ASCII (``asc/``) and as HDF5. The HDF5 file is
not kept; ``oracle.json`` holds what simapy's HDF5 reader -- checked against SIMA in
``test_results_oracle.py`` -- reads from it for a spread of each storage file's signals:

* ``guide``: SIMA's guide example riser (R344) with the storage of R705, every line response
* ``pisa``: piles in PISA soil (R566), seafloor contact in soil units
* ``turbine``: two DTU 10 MW turbines (R340), turbine and blade response
* ``wavkin``, ``updkin``: a steel riser (R304), pre-generated and updated wave kinematics

Key files RIFLEX no longer writes (no contact column, one turbine, no column header) are
made from these by removing what the newer format added.
"""

import json
import shutil
import warnings
from pathlib import Path

import numpy as np
import pytest

from simapy_results import Container, Signal, Status, UnsupportedStorageWarning, copy_results, open_results
from simapy_results._units import base_unit

DATA = Path(__file__).parent / "data" / "riflex_storage"
GUIDE = DATA / "guide"
CASES = ("guide", "pisa", "turbine", "wavkin", "updkin")

FORCES = ("Axial force", "Torsional moment",
          "Mom. about local y-axis, end 1", "Mom. about local y-axis, end 2",
          "Mom. about local z-axis, end 1", "Mom. about local z-axis, end 2",
          "Shear force in local y-direction, end 1", "Shear force in local y-direction, end 2",
          "Shear force in local z-direction, end 1", "Shear force in local z-direction, end 2")
FORCE_UNITS = ("N", "N*m", "N*m", "N*m", "N*m", "N*m", "N", "N", "N", "N")


def _oracle(case: str) -> dict:
    return json.loads((DATA / case / "oracle.json").read_text(encoding="utf-8"))


def _storage(fmt: str) -> list[tuple[str, str, Path]]:
    """Every storage file but the element transformations, whose signals need riflexres.inp."""
    return [(case, path.stem, path) for case in CASES
            for path in sorted((DATA / case / fmt).glob(f"*.{fmt}"))
            if not path.stem.endswith("_elmtra")]


def _dynamic(path: Path) -> Container:
    res = open_results(path)
    assert [s.status for s in res.sources] == [Status.READ], res.sources
    return res.run.container("Dynamic")


def _flatten(container: Container) -> dict[str, Signal]:
    """Signals by path below the container."""
    prefix = len(container.path) + 1
    return {node.path[prefix:]: node for node in container.walk() if isinstance(node, Signal)}


def _matches(signal: Signal, expected: dict) -> None:
    # The HDF5 reader cancels a moment per length, N*m/m, to N; SIMA's storage labels do not.
    assert base_unit(signal.unit) == base_unit(expected["unit"])
    assert len(signal) == expected["size"]
    assert signal.xunit == "s"
    assert signal.xstart == pytest.approx(expected["xstart"])
    assert signal.xdelta == pytest.approx(expected["xdelta"])
    y = np.asarray(expected["y"])
    assert signal.y == pytest.approx(y, rel=1e-5, abs=1e-6 * max(1.0, float(np.abs(y).max())))


def _copy(tmp_path: Path, *names: str, source: Path = GUIDE / "bin") -> Path:
    folder = tmp_path / "Task" / "Condition"
    folder.mkdir(parents=True)
    for name in names:
        for file in source.glob(f"*{name}*"):
            shutil.copy2(file, folder / file.name)
    return folder


def _riflexres(folder: Path, *, relative=(), angles=(), read_matrix=False,
               units=("W=kW", "M=Mg", "F=kN", "P=kPa"), vessels=()) -> None:
    """A ``riflexres.inp`` as ``RIFLEXResultMapperExporter`` writes one."""
    rows = ["'Version", "2.6.0", "'Number of line name mappings", "1", "riser_l3=riser_l3", "0",
            "'Number of relative angle specifications", str(len(relative))]
    for element, references in relative:
        rows += ["'Element", *map(str, element), "'Element angle refences", str(len(references))]
        for reference in references:
            rows += [*map(str, reference)]
    rows += ["'Number of element angle specifications", str(len(angles))]
    for element, plane, axis in angles:
        rows += [*map(str, element), plane, axis]
    rows += ["'Number of element force transformations", "0",
             "'Number of stress storage specifications", "0",
             "'Load steps", "0", "'nIDs", "0",
             "'nParams", "1", "'Parameters", f"readMatrix={str(read_matrix).lower()}",
             "'Exported units", "'NUNITS", str(len(units)), *units,
             "'Number of support vessels", str(len(vessels)), *vessels]
    (folder / "riflexres.inp").write_text("\n".join(rows) + "\n", encoding="utf-8")


def _rewrite_key(folder: Path, stem: str, rewrite) -> None:
    key = folder / f"key_{stem}.txt"
    lines = key.read_bytes().decode("latin-1").splitlines()
    key.write_bytes("\n".join(rewrite(lines)).encode("latin-1") + b"\n")


# -- every storage file agrees with RIFLEX's HDF5 storage of the same run ------------


@pytest.mark.parametrize("case, stem, path", _storage("bin") + _storage("asc"),
                         ids=lambda v: v.name if isinstance(v, Path) else None)
def test_storage_matches_hdf5(case, stem, path):
    expected = _oracle(case)[stem]
    signals = _flatten(_dynamic(path))

    for name, entry in expected.items():
        assert name in signals, f"{name} missing; have {sorted(signals)[:5]}"
        _matches(signals[name], entry)


@pytest.mark.parametrize("case", CASES)
def test_ascii_matches_binary(case):
    """Same tree, names, units and axes; values within float32 rounding."""
    for _, _, data in (s for s in _storage("asc") if s[0] == case):
        binary = _flatten(_dynamic(DATA / case / "bin" / f"{data.stem}.bin"))
        ascii_ = _flatten(_dynamic(data))
        assert list(ascii_) == list(binary), data.name
        for name, expected in binary.items():
            actual = ascii_[name]
            assert (actual.unit, len(actual), dict(actual.attributes)) == \
                (expected.unit, len(expected), dict(expected.attributes)), name
            assert actual.xstart == pytest.approx(expected.xstart), name
            assert actual.xdelta == pytest.approx(expected.xdelta), name
            scale = max(1.0, float(np.abs(expected.y).max()))
            assert actual.y == pytest.approx(expected.y, rel=1e-6, abs=1e-6 * scale), name


# -- the tree, names and units each key-file layout gives ---------------------------------


def test_forces():
    element = _dynamic(GUIDE / "bin" / "guide_elmfor.bin").container("riser_l3/segment_9/element_1")

    line = element.parent.parent
    assert (line.name, line.type) == ("riser_l3", "line")
    assert (element.parent.name, element.parent.type, element.parent.attributes["index"]) == \
        ("segment_9", "segment", "9")
    assert (element.type, element.attributes["index"]) == ("element", "1")
    assert [(s.name, s.unit) for s in element.signals] == list(zip(FORCES, FORCE_UNITS))
    assert all(s.attributes["element"] == "element_1" for s in element.signals)
    assert [e.name for e in element.parent.containers] == ["element_1", "element_2"]


def test_displacements_curvature_and_sum_forces():
    node = _dynamic(GUIDE / "bin" / "guide_noddis.bin").container("riser_l3/segment_9/node_1")
    curvature = _dynamic(GUIDE / "bin" / "guide_elmcur.bin").container("riser_l3/segment_9/element_1")
    summed = _dynamic(GUIDE / "bin" / "guide_elmsfo.bin").container("riser_l3/segment_9/element_1")

    assert node.type == "node"
    assert [(s.name, s.unit, s.attributes["node"]) for s in node.signals] == [
        (f"Displacement in {axis} - direction", "m", "node_1") for axis in "xyz"]
    assert [(s.name, s.unit) for s in curvature.signals] == [
        (f"Curvature about local {axis}-axis, end {end}", "1/m") for axis in "yz" for end in (1, 2)]
    assert [(s.name, s.unit) for s in summed.signals] == [("Axial sum force", "N")]


def test_contact_forces_name_their_contact():
    """The key file's last column names the contact (sima/issue#944)."""
    nodes = _dynamic(GUIDE / "bin" / "guide_cntfor.bin").container("riser_l3/segment_9").containers

    assert len(nodes) == 80
    assert [(s.name, s.unit) for s in nodes[0].signals[:4]] == [
        ("Contact force in local x-direction - ri_bm_1", "N"),
        ("Contact force in local y-direction - ri_bm_1", "N"),
        ("Contact force in local z-direction - ri_bm_1", "N"),
        ("Moment about local x-axis - ri_bm_1", "N*m")]


def test_contact_forces_without_a_contact_column_are_numbered(tmp_path):
    """A key file from before the column names a node's contacts by their order."""
    folder = _copy(tmp_path, "guide_cntfor")
    _rewrite_key(folder, "guide_cntfor", lambda lines: [
        line.rsplit(None, 1)[0] if line.startswith(" riser_l3") else line for line in lines])

    node = _dynamic(folder / "guide_cntfor.bin").container("riser_l3/segment_9/node_1")

    assert node.signals[0].name == "Contact force in local x-direction - Contact 1"


def test_hydrodynamic_loads():
    element = _dynamic(GUIDE / "bin" / "guide_hydloa.bin").container("riser_l3/segment_9/element_1")

    loads = [("Hydrodynamic load, global x direction", "N/m"),
             ("Hydrodynamic load, global y direction", "N/m"),
             ("Hydrodynamic load, global z direction", "N/m"),
             ("Hydrodynamic load, moment around global x axis", "N*m/m"),
             ("Hydrodynamic load, moment around global y axis", "N*m/m"),
             ("Hydrodynamic load, moment around global z axis", "N*m/m")]
    assert [(s.name, s.unit) for s in element.signals] == [
        (f"{name}, end {end}", unit) for end in (1, 2) for name, unit in loads]


def test_general_storage_without_a_column_header(tmp_path):
    """Before the ``0 LINE LSEG ...`` header row, the columns came in a fixed order."""
    folder = _copy(tmp_path, "guide_hydloa")
    _rewrite_key(folder, "guide_hydloa",
                 lambda lines: [line for line in lines if line.split()[:2] != ["0", "LINE"]])

    original = _flatten(_dynamic(GUIDE / "bin" / "guide_hydloa.bin"))
    rewritten = _flatten(_dynamic(folder / "guide_hydloa.bin"))

    assert list(rewritten) == list(original)
    assert [s.unit for s in rewritten.values()] == [s.unit for s in original.values()]


def test_seafloor_contact():
    element = _dynamic(GUIDE / "bin" / "guide_botres.bin").container("riser_l3/segment_9/element_1")

    assert [(s.name, s.unit) for s in element.signals[:6]] == [
        ("Axial spring elongation - End 1", "m"),
        ("Lateral spring elongation - End 1", "m"),
        ("Indentation into seafloor - End 1", "m"),
        ("Axial stiffness per length - End 1", "N/m^2"),
        ("Lateral stiffness per length - End 1", "N/m^2"),
        ("Normal stiffness per length - End 1", "N/m^2")]


def test_seafloor_contact_in_soil():
    dynamic = _dynamic(DATA / "pisa" / "bin" / "soil_PISA_botres.bin")

    assert [line.name for line in dynamic.containers] == ["pile1", "pile2", "pile3", "pile4"]
    units = {s.name.rsplit(" - End", 1)[0]: s.unit for s in _flatten(dynamic).values()}
    assert units["SLP rotation from reference orientation"] == "deg"
    assert units["SLP rotational stiffness"] == "N*m/deg"
    assert units["SLP rotational stiffness per length"] == "N*m/m*deg"
    assert units["SLP lateral stiffness per length"] == "N/m^2"
    assert units["SLP moment per length"] == "N*m/m"


@pytest.mark.parametrize("case, size", [("wavkin", 64), ("updkin", 11)])
def test_wave_kinematics(case, size):
    dynamic = _dynamic(DATA / case / "bin" / f"slow4_{case}.bin")

    node = dynamic.container("1/segment_2/node_30")
    assert node.type == "node"
    assert [(s.name, s.unit) for s in node.signals] == [
        ("Wave elevation", "m"),
        *[(f"Fluid velocity, global {axis}-direction", "m/s") for axis in "XYZ"],
        *[(f"Fluid acceleration, global {axis}-direction", "m/s^2") for axis in "XYZ"],
        ("Fluid dynamic pressure", "N/m^2")]
    assert {len(s) for s in node.signals} == {size}


def test_wave_kinematics_at_a_supernode(tmp_path):
    """A supernode's kinematics sit on the supernode itself, typed as one."""
    folder = _copy(tmp_path, "slow4_wavkin", source=DATA / "wavkin" / "bin")

    def to_supernode(lines):
        out = []
        for line in lines:
            tokens = line.split()
            if len(tokens) > 4 and tokens[1] == "LINE" and tokens[3:5] == ["2", "30"]:
                line = line.replace(" LINE ", " SNOD ", 1).replace(" 1 ", " top ", 1)
                tokens = line.split()
                tokens[2:5] = ["top", "-", "-"]
                line = "  ".join(tokens)
            out.append(line)
        return out

    _rewrite_key(folder, "slow4_wavkin", to_supernode)

    dynamic = _dynamic(folder / "slow4_wavkin.bin")

    top = dynamic.container("top")
    assert top.type == "supernode"
    assert [s.name for s in top.signals][:2] == ["Wave elevation", "Fluid velocity, global X-direction"]
    assert "node_30" not in dynamic.container("1/segment_2")


def test_wind_turbines():
    turbines = _dynamic(DATA / "turbine" / "bin" / "dtu10mw_witurb.bin").containers

    assert [t.name for t in turbines] == ["Turbine1", "Turbine2"]
    signals = {s.name: s for s in turbines[0].signals}
    assert signals["Rotor speed"].unit == "deg/s"
    rpm = signals["Rotor speed (rpm)"]
    assert rpm.unit == "rpm"
    assert rpm.y == pytest.approx(signals["Rotor speed"].y / 6.0)
    assert signals["Electrical generator output"].unit == "W"
    assert signals["Pitch angle blade 1, Line: bl1foil1"].unit == "deg"


def test_one_wind_turbine_in_the_older_key_file(tmp_path):
    """Without a turbine column the signals go in one container, "Wind Turbine"."""
    folder = _copy(tmp_path, "dtu10mw_witurb", source=DATA / "turbine" / "bin")

    def without_turbine_column(lines):
        out = []
        for line in lines:
            tokens = line.split()
            if len(tokens) > 3 and tokens[0].isdigit() and int(tokens[0]) > 1:
                line = " ".join([tokens[0], *tokens[2:]])
            out.append(line)
        return out

    _rewrite_key(folder, "dtu10mw_witurb", without_turbine_column)

    turbines = _dynamic(folder / "dtu10mw_witurb.bin").containers

    assert [t.name for t in turbines] == ["Wind Turbine"]
    assert [s.name for s in turbines[0].signals[:2]] == ["Rotor speed", "Rotor speed (rpm)"]
    assert len(turbines[0].signals) == 2 * 24


def test_blade_response():
    element = _dynamic(DATA / "turbine" / "bin" / "dtu10mw_blresp.bin").container(
        "bl2foil1/segment_5/element_1")

    assert element.type == "element"
    units = {s.name: s.unit for s in element.signals}
    assert units["Lift force intensity in foil system"] == "N/m"
    assert units["Moment intensity in foil system"] == "N*m/m"
    assert units["Angle of attack in foil system"] == "deg"


# -- what riflexres.inp adds --------------------------------------------------------------


def _hdf5_matrix(element: str) -> np.ndarray:
    """RIFLEX's own local-to-global matrices from HDF5, as [step, row, column]."""
    stored = _oracle("guide")["transformations"]
    prefix = f"riser_l3/segment_9/{element}/Transformation matrix from local to global/T"
    return np.stack([[np.asarray(stored[f"{prefix}{r}{c}"]["y"]) for c in (1, 2, 3)]
                     for r in (1, 2, 3)]).transpose(2, 0, 1)


@pytest.mark.parametrize("fmt", ["bin", "asc"])
def test_transformation_matrix_is_riflex_s(fmt, tmp_path):
    folder = _copy(tmp_path, "guide_elmtra", source=GUIDE / fmt)
    _riflexres(folder, read_matrix=True)

    dynamic = _dynamic(folder / f"guide_elmtra.{fmt}")

    for element in ("element_1", "element_2"):
        matrix = dynamic.container(f"riser_l3/segment_9/{element}/Transformation matrix from local to global")
        assert [s.name for s in matrix.signals] == [f"T{r}{c}" for r in (1, 2, 3) for c in (1, 2, 3)]
        got = np.stack([[matrix.signal(f"T{r}{c}").y for c in (1, 2, 3)]
                        for r in (1, 2, 3)]).transpose(2, 0, 1)
        assert got == pytest.approx(_hdf5_matrix(element), abs=1e-6)


@pytest.mark.parametrize("fmt", ["bin", "asc"])
def test_element_angles(fmt, tmp_path):
    folder = _copy(tmp_path, "guide_elmtra", source=GUIDE / fmt)
    _riflexres(folder, relative=[(("riser_l3", 9, 1), [("riser_l3", 9, 2)])],
               angles=[(("riser_l3", 9, 1), "YZ", "Z"), (("riser_l3", 9, 1), "XZ", "X")])

    element = _dynamic(folder / f"guide_elmtra.{fmt}").container("riser_l3/segment_9/element_1")

    relative, yz, xz = element.signals
    assert [(s.name, s.unit) for s in element.signals] == [
        ("Relative angle to riser_l3, segment 9, element 2", "deg"),
        ("Angle with Z axis, projected in YZ plane", "deg"),
        ("Angle with X axis, projected in XZ plane", "deg")]
    first, second = _hdf5_matrix("element_1"), _hdf5_matrix("element_2")
    # The angle between the two elements' local x-axes, the matrices' first columns.
    dot = np.clip(np.einsum("ti,ti->t", first[:, :, 0], second[:, :, 0]), -1, 1)
    assert relative.y == pytest.approx(np.degrees(np.arccos(dot)), abs=1e-3)
    assert yz.y == pytest.approx(np.degrees(np.arctan2(first[:, 1, 0], first[:, 2, 0])), abs=1e-3)
    assert xz.y == pytest.approx(np.degrees(np.arctan2(first[:, 2, 0], first[:, 0, 0])), abs=1e-3)


def test_a_relative_angle_to_an_element_not_stored_fails_the_file(tmp_path):
    folder = _copy(tmp_path, "guide_elmtra")
    _riflexres(folder, relative=[(("riser_l3", 9, 1), [("riser_l3", 9, 3)])])

    with pytest.warns(UserWarning, match="not able to find storage of line riser_l3 segment 9 element 3"):
        res = open_results(folder / "guide_elmtra.bin")

    assert [s.status for s in res.sources] == [Status.FAILED]


@pytest.mark.parametrize("fmt", ["bin", "asc"])
def test_support_force(fmt, tmp_path):
    folder = _copy(tmp_path, "guide_supportforce", source=GUIDE / fmt)

    assert _dynamic(folder / f"guide_supportforce.{fmt}").containers[0].name == "1", \
        "support vessel 1, unnamed without riflexres.inp"

    _riflexres(folder, vessels=("pltfrm",))
    dynamic = _dynamic(folder / f"guide_supportforce.{fmt}")

    body = dynamic.containers[0]
    assert (body.name, body.type, body.attributes["body"]) == ("pltfrm", "body", "pltfrm")
    assert [n.name for n in body.container("Slender system forces").containers] == ["ris_hang", "bellm_f"]
    signals = _flatten(dynamic)
    for name, entry in _oracle("guide")["supportforce_hdf5"].items():
        _matches(signals[name], entry)


def test_units_come_from_riflexres(tmp_path):
    """A model exported in N writes N; scaling it as kN would be off by 1000."""
    folder = _copy(tmp_path, "guide_elmfor")
    _riflexres(folder, units=("W=W", "M=kg", "F=N", "P=Pa"))

    axial = _dynamic(folder / "guide_elmfor.bin").signal("riser_l3/segment_9/element_1/Axial force")

    in_kn = _oracle("guide")["guide_elmfor"]["riser_l3/segment_9/element_1/Axial force"]["y"]
    assert axial.y == pytest.approx(np.asarray(in_kn) / 1000, rel=1e-5)


# -- a folder of storage --------------------------------------------------------------------


@pytest.mark.parametrize("fmt", ["bin", "asc"])
def test_a_run_folder_opens_cleanly(fmt):
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        res = open_results(GUIDE / fmt)

    assert len(res.sources) == (9 if fmt == "bin" else 8)
    assert all(s.status is Status.READ for s in res.sources), res.sources
    dynamic = res.run.container("Dynamic")
    assert dynamic.type == "dynamic"
    assert [c.name for c in dynamic.containers] == ["1", "riser_l3", "riser_l1"]
    # 30 steps of 0.1 s: seafloor contact stored at each, the rest at every tenth.
    element = dynamic.container("riser_l3/segment_9/element_1")
    assert sorted({(len(s), s.xdelta) for s in element.signals}) == [
        (3, pytest.approx(1.0)), (30, pytest.approx(0.1))]


@pytest.mark.parametrize("fmt", ["bin", "asc"])
def test_a_node_is_one_frame(fmt):
    pytest.importorskip("pandas")

    node = open_results(GUIDE / fmt).run.container("Dynamic/riser_l3/segment_9/node_1")

    assert node.to_dataframe().shape == (3, len(node.signals))


def test_storage_files_merge_into_one_tree(tmp_path):
    folder = _copy(tmp_path, "guide_elmfor", "guide_noddis", "guide_elmcur")

    res = open_results(folder)

    assert {s.file: s.status for s in res.sources} == {
        "guide_elmcur.bin": Status.READ, "guide_elmfor.bin": Status.READ,
        "guide_noddis.bin": Status.READ}
    segment = res.run.container("Dynamic/riser_l3/segment_9")
    assert [c.name for c in segment.containers] == ["element_1", "element_2", "node_1"]
    assert len(segment.container("element_1").signals) == 10 + 4


def test_nothing_is_read_before_it_is_asked_for(monkeypatch):
    from simapy_results._readers import riflex_storage  # pylint: disable=import-outside-toplevel

    reads = []
    original = riflex_storage._Data.matrix
    monkeypatch.setattr(riflex_storage._Data, "matrix",
                        lambda self: reads.append(self.path.name) or original(self))

    signals = list(_flatten(open_results(GUIDE / "bin" / "guide_elmfor.bin").run).values())
    assert [(len(s), s.unit, s.xstart) for s in signals[:1]] == [(3, "N", pytest.approx(1.0))]
    assert reads == []

    _ = signals[0].y
    _ = signals[1].y
    assert reads == ["guide_elmfor.bin", "guide_elmfor.bin"]


def test_values_are_read_only():
    signal = _dynamic(GUIDE / "bin" / "guide_elmfor.bin").signal("riser_l3/segment_9/element_1/Axial force")

    with pytest.raises(ValueError, match="read-only"):
        signal.y[0] = 1.0


def test_a_binary_file_whose_records_disagree_with_its_key_fails(tmp_path):
    folder = _copy(tmp_path, "guide_elmfor")
    content = (folder / "guide_elmfor.bin").read_bytes()
    (folder / "guide_elmfor.bin").write_bytes(content[:-4])

    with pytest.warns(UserWarning, match="not whole steps"):
        res = open_results(folder / "guide_elmfor.bin")

    assert [s.status for s in res.sources] == [Status.FAILED]


def test_storage_files_are_copied_with_their_key_files(tmp_path):
    condition = tmp_path / "Task" / "Condition"
    shutil.copytree(GUIDE / "bin", condition / "1-20261021102800")
    (condition / "results.json").write_text(
        '{"task": "Task", "condition": "Condition", '
        '"directories": {"Dynamic": "1-20261021102800"}}', encoding="utf-8")

    copy_results(condition, tmp_path / "copy")

    res = open_results(tmp_path / "copy")
    assert len(res.sources) == 9
    assert all(s.status is Status.READ for s in res.sources), res.sources


def test_storage_without_a_key_file_is_no_result(tmp_path):
    """RIFLEX's turbulence boxes and FEM files share the extensions; only storage has a key file."""
    folder = _copy(tmp_path, "guide_elmfor")
    shutil.copy2(folder / "guide_elmfor.bin", folder / "wind_u.bin")
    (folder / "sima_eledat.asc").write_text("1 2 3\n", encoding="utf-8")

    with warnings.catch_warnings():
        warnings.simplefilter("error", UnsupportedStorageWarning)
        res = open_results(folder)

    assert [s.file for s in res.sources] == ["guide_elmfor.bin"]
