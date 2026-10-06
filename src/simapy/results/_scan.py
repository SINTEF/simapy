"""Work out what a run folder holds, from the folder.

Three files beside the results carry what is not itself a result: ``names.map``
(hashed model id to real name), ``results.json`` (which task and condition
produced them, and the variables with their units) and ``variables.inp`` (the
values alone, read only when ``results.json`` gives none). Only the result files
are required; without the others, ids stay hashed, units read ``-`` and the names
come from the path.

A working directory is read as it is. A whole condition is read only as its
``results.json`` maps it (:func:`describe_condition`): nothing else on disk says
which of several working directories hold the current runs.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterator

from ._description import Entry, ResultFile, ResultsError, RunDescription, Variable
from ._registry import find_reader

#: Hashed model id to real name. Alternating lines: short, long, short, long.
ID_MAP_FILENAME = "names.map"

#: The variable values a run used.
VARIABLES_FILENAME = "variables.inp"

#: Which task and condition produced the results, and the variable units. The
#: solvers write neither, and the folder path stops being true once results move.
RESULTS_FILENAME = "results.json"

#: Extensions a scan will not claim, however well a reader reads them. A
#: workflow writes its input and its output as the same signals model in one
#: folder, and nothing in either says which it is.
_NOT_BY_SCAN: frozenset[str] = frozenset({".json"})


def is_result(path: Path) -> bool:
    """Whether a folder scan offers this file as a result."""
    return (
        path.is_file()
        and path.suffix.lower() not in _NOT_BY_SCAN
        and not is_internal(path.name)
        and find_reader(path) is not None
    )


def _both(stem: str, suffix: str = ".h5") -> frozenset[str]:
    """Both spellings of one name: plain SIMO, and ``-sima`` for RIFLEX-coupled."""
    return frozenset({f"{stem}{suffix}", f"{stem}-sima{suffix}"})


#: Working files the solvers leave beside the results. Exact names, not extensions.
_INTERNAL: frozenset[str] = frozenset(
    _both("simo")
    | _both("simo-intermediate")
    | _both("simstab-intermediate")
    | _both("simo-static-results")
    | _both("simo-dynamic-results")
    | {"env.h5"}
)

#: Two of those six are results despite the name. Missing either loses a whole
#: analysis, so the exclusion above does not apply to them.
_RESULTS_ANYWAY: frozenset[str] = _both("simo-static-results") | _both(
    "simo-dynamic-results"
)


#: SIMO's static results as text, which SIMA copies into the dynamic folder.
_PSC: frozenset[str] = _both("psc", ".lis")


def _in_sima_order(results: list[ResultFile]) -> tuple[ResultFile, ...]:
    """SIMOStaticResultFactory registers psc.lis after the HDF5, and sibling order follows read order."""
    return tuple(sorted(results, key=lambda result: Path(result.file).name.lower() in _PSC))


def is_internal(name: str) -> bool:
    """Whether this file is working data rather than a result.

    Compared lowercased, so a difference in case cannot turn an intermediate
    into a result on a case-insensitive file system.
    """
    lower = name.lower()
    return lower in _INTERNAL and lower not in _RESULTS_ANYWAY


#: Name fragment to (entry, runType); declaration order is precedence. Only
#: files a reader claims reach this, so a new reader may need fragments adding
#: here -- and one whose files can be copied between run folders needs checking
#: against that, since a fragment alone would then name the wrong run.
_PHASES: tuple[tuple[str, str, str], ...] = (
    ("stamod", "Static", "static"),
    ("simo-static-results", "Static", "static"),
    ("psc", "Static", "static"),
    ("dynmod", "Dynamic", "dynamic"),
    ("simo-dynamic-results", "Dynamic", "dynamic"),
    ("ts_buffer", "Dynamic", "dynamic"),
    ("noddis", "Dynamic", "dynamic"),
    ("elmfor", "Dynamic", "dynamic"),
    ("elmcur", "Dynamic", "dynamic"),
    ("eigmod", "Eigenvalue", "eigenvalue"),
    ("vivana", "Vivana", "vivana"),
    # SIMA holds OUTMOD results in the dynamic entry (RIFLEXDynamicResultEntry.outmodResuls).
    ("outmod", "Dynamic", "dynamic"),
)

#: Entry order in the description, and so child order in the tree.
_ENTRY_ORDER: tuple[str, ...] = ("Static", "Dynamic", "Eigenvalue", "Vivana")

#: ``<runNumber>-<yyyyMMddHHmmss>``, the working-directory name SIMA builds
#: when the timestamp preference is on.
_RUN_DIR = re.compile(r"\A\d+-\d{14}\Z")

#: ``variables.inp`` names its block by the model reference it came from, which
#: is what keeps an integer variable from coming back as a float.
_VARIABLE_TYPES: dict[str, type] = {
    "doubleVariables": float,
    "integerVariables": int,
    "stringVariables": str,
    "referenceVariables": str,
}


def find_runs(condition: str | Path) -> list[Path]:
    """The working directories of a condition ``<workspace>/<task>/<condition>``.

    The condition folder itself when results sit directly in it, then one
    timestamped folder per run, or its members for a condition set. Empty for a
    condition that has not been run.
    """
    path = Path(condition).absolute()
    if not path.is_dir():
        return []
    found = [path] if holds_results(path) else []
    for run in sorted(p for p in path.iterdir() if p.is_dir() and _RUN_DIR.match(p.name)):
        if holds_results(run):
            found.append(run)
        else:
            found.extend(sorted(p for p in run.iterdir() if p.is_dir() and holds_results(p)))
    return found


def holds_results(folder: str | Path) -> bool:
    """Whether opening ``folder`` would read at least one result file."""
    path = Path(folder)
    return path.is_dir() and bool(_entries(path))


def phase_of(name: str) -> tuple[str, str] | None:
    """The entry and runType a file belongs to, or None if its name says nothing.

    Grouping by analysis is correctness, not tidiness: one folder can hold both
    a static and a dynamic result whose containers have the same names, and a
    flat entry would merge one into the other.
    """
    lower = name.lower()
    for fragment, entry, run_type in _PHASES:
        if fragment in lower:
            return entry, run_type
    return None


def read_run(folder: Path) -> tuple[str | None, str | None]:
    """The task and condition ``results.json`` names, or ``(None, None)``."""
    return _run_of(list(_manifests(Path(folder).absolute())))


def _run_of(manifests: list[dict]) -> tuple[str | None, str | None]:
    """The nearest manifest naming a task or condition wins; unreadable values degrade to None."""
    for content in manifests:
        task = content.get("task")
        condition = content.get("condition")
        if task or condition:
            return (task if isinstance(task, str) else None,
                    condition if isinstance(condition, str) else None)
    return None, None


def read_manifest_variables(folder: Path) -> dict[str, Variable] | None:
    """The run's variables from ``results.json``, or None when no manifest gives them."""
    path = Path(folder).absolute()
    return _variables_for(list(_manifests(path)), path.name, is_member(path))


def _variables_for(manifests: list[dict], folder: str, member: bool) -> dict[str, Variable] | None:
    """Values and units together, nearest manifest first.

    A set records the variables it holds constant at the top and each member's
    own under ``conditions``; the member wins where both name one. A member
    folder the set does not list gets None rather than only the constants.
    """
    for content in manifests:
        if member:
            members = content.get("conditions")
            if not isinstance(members, list):
                continue
            own = next((entry for entry in members
                        if isinstance(entry, dict) and entry.get("condition") == folder), None)
            if own is None:
                return None
            return {**_variables_of(content.get("variables")), **_variables_of(own.get("variables"))}
        if "variables" in content:
            return _variables_of(content.get("variables"))
    return None


def _variables_of(values: object) -> dict[str, Variable]:
    if not isinstance(values, dict):
        return {}
    variables = {}
    for name, entry in values.items():
        if not isinstance(entry, dict) or "value" not in entry:
            continue
        unit = entry.get("unit")
        variables[name] = Variable(entry["value"], unit if isinstance(unit, str) and unit else None)
    return variables


def _manifests(folder: Path) -> Iterator[dict]:
    """Each readable ``results.json`` from the folder upward, nearest first.

    Three levels reach the condition from one of its set members.
    """
    current = folder
    for _ in range(3):
        content = _read_manifest(current / RESULTS_FILENAME)
        if content is not None:
            yield content
        if current == current.parent:
            return
        current = current.parent


def _read_manifest(path: Path) -> dict | None:
    try:
        content = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return content if isinstance(content, dict) else None


def is_member(folder: Path) -> bool:
    """Whether this is one member of a condition set, which sits below a run folder."""
    return bool(_RUN_DIR.match(folder.parent.name))


def read_names(folder: Path) -> dict[str, str]:
    """Hashed id to model name, from ``names.map`` and ``riflexres.inp``.

    ``riflexres.inp`` wins where both name an id: it is what SIMA's MPF import
    reads, and RIFLEX writes it beside every run, where a static run on its own
    leaves no ``names.map``. Without either, ids stay hashed (``line Risea63d``)
    -- cosmetic, never a failure, so a file that does not parse adds no names
    rather than half a map.
    """
    return {**_read_id_map(folder), **_read_riflex_ids(folder)}


#: Line and other model names, written by RIFLEX's ``RIFLEXResultMapperExporter``.
RIFLEX_MAPPER_FILENAME = "riflexres.inp"


def _read_riflex_ids(folder: Path) -> dict[str, str]:
    """The ids ``RIFLEXResultMapperImporter`` maps: the line names, then ``readIds``.

    The sections in between are walked as that importer walks them, only to
    reach the ids after them.
    """
    try:
        text = (folder / RIFLEX_MAPPER_FILENAME).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}
    rows = iter(line for line in text.splitlines() if not line.startswith("'"))
    ids: dict[str, str] = {}
    try:
        version = tuple(int(part) for part in next(rows).strip().split("."))
        if version < (2, 0, 0):
            return {}
        for _ in range(int(next(rows))):
            key, value = _key_value(next(rows))
            ids[key] = value
            if version >= (2, 1, 0):
                for _ in range(int(next(rows))):  # segments
                    _skip(rows, int(next(rows)))  # their properties
        for _ in range(int(next(rows))):  # relative angles
            _skip(rows, 3)
            _skip(rows, 3 * int(next(rows)))
        _skip(rows, 5 * int(next(rows)))  # element angles
        if version >= (2, 6, 0):
            _skip(rows, 4 * int(next(rows)))  # transformations
        _skip(rows, 2 * int(next(rows)))  # stress storage
        if version >= (2, 1, 0):
            _skip(rows, 2 * int(next(rows)))  # load steps
        if version >= (2, 2, 0):
            for _ in range(int(next(rows))):
                key, value = _key_value(next(rows))
                ids[key] = value
    except (StopIteration, ValueError, IndexError):
        return {}
    return ids


def _key_value(row: str) -> tuple[str, str]:
    parts = row.split("=")
    return parts[0], parts[1]


def _skip(rows: Iterator[str], count: int) -> None:
    for _ in range(count):
        next(rows)


def _read_id_map(folder: Path) -> dict[str, str]:
    try:
        lines = [
            line.strip()
            for line in (folder / ID_MAP_FILENAME)
            .read_text(encoding="utf-8")
            .splitlines()
        ]
    except (OSError, UnicodeDecodeError):
        return {}
    lines = [line for line in lines if line]
    if not lines or len(lines) % 2:
        return {}
    return dict(zip(lines[::2], lines[1::2]))


def read_variables(folder: Path) -> tuple[str | None, dict[str, Variable]]:
    """The task name and variable values from ``variables.inp``, which has no units.

    One block per model reference::

        'Simple_Flexible_Riser.doubleVariables
        'Number of variables
        2
        'Variable=Value
        hs=1.1
        tp=10.0

    The header names the task and the reference; the reference types the value,
    and the task name beats any folder name because a member's folders sit under
    the set rather than the task.

    Parsed tolerantly -- counts and block order are ignored in favour of the
    lines themselves, since the format is observed rather than specified.
    """
    try:
        text = (folder / VARIABLES_FILENAME).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None, {}

    task: str | None = None
    convert: type = str
    variables: dict[str, Variable] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("'"):
            head, dot, reference = line[1:].rpartition(".")
            if dot and reference in _VARIABLE_TYPES:
                task = task or head
                convert = _VARIABLE_TYPES[reference]
            continue
        name, sep, value = line.partition("=")
        if not sep:
            continue  # the variable count, or anything else unlabelled
        try:
            variables[name.strip()] = Variable(convert(value.strip()))
        except ValueError:
            # Keep the value rather than the type: a number that will not parse
            # is still what the run used.
            variables[name.strip()] = Variable(value.strip())
    return task, variables


def _identify(folder: Path) -> tuple[str, str]:
    """The task and condition names the folder path implies.

    The layout is ``<workspace>/<task>/<condition>``, optionally with a
    timestamp folder under the condition and, for a set member, one more level
    under that. Skipping a timestamp-shaped name is what lets a working
    directory report the condition it belongs to rather than calling itself
    ``1-20260901063413``.
    """
    names: list[str] = []
    current = folder
    while current != current.parent and len(names) < 2:
        if current.name and not _RUN_DIR.match(current.name):
            names.append(current.name)
        current = current.parent
    condition = names[0] if names else "condition"
    task = names[1] if len(names) > 1 else "task"
    return task, condition


def _entries(folder: Path) -> tuple[Entry, ...]:
    """The result files in ``folder``, grouped by the analysis that made them.

    Only what some reader claims: a folder cannot tell a result nothing here
    reads from a solver input, so such a file is left out rather than reported.
    ``psc.lis`` counts only beside another static result: SIMA copies it into
    every dynamic folder.
    """
    grouped: dict[str, list[ResultFile]] = {}
    run_types: dict[str, str] = {}
    unmatched: list[ResultFile] = []

    for child in sorted(folder.iterdir()):
        if not is_result(child):
            continue
        result = ResultFile(file=child.name)
        phase = phase_of(child.name)
        if phase is None:
            unmatched.append(result)
            continue
        entry, run_type = phase
        grouped.setdefault(entry, []).append(result)
        run_types[entry] = run_type

    static = grouped.get("Static", [])
    if static and all(r.file.lower() in _PSC for r in static):
        del grouped["Static"]

    entries = [
        Entry(name=entry, run_type=run_types[entry], results=_in_sima_order(grouped[entry]))
        for entry in _ENTRY_ORDER
        if entry in grouped
    ]
    if unmatched:
        entries.append(Entry(name="", container=False, results=tuple(unmatched)))
    return tuple(entries)


def describe_file(
    path: str | Path, *, names: dict[str, str] | None = None,
    task: str | None = None, condition: str | None = None,
) -> RunDescription:
    """Describe one result file, as if its folder held only that file.

    The folder's ``results.json``, ``variables.inp`` and ``names.map`` still
    apply, so the tree matches opening the folder, minus the other files.

    :raises ResultsError: if no reader claims the file.
    """
    file = Path(path).absolute()
    if find_reader(file) is None:
        raise ResultsError(f"no reader for {file.name}")
    return _describe(file.parent, (_entry_for(ResultFile(file=file.name)),),
                     names, task, condition)


def _entry_for(result: ResultFile) -> Entry:
    """The entry one result file belongs in, named by the analysis that made it."""
    phase = phase_of(result.file)
    if phase is None:
        return Entry(name="", container=False, results=(result,))
    name, run_type = phase
    return Entry(name=name, run_type=run_type, results=(result,))


def describe(
    folder: str | Path, *, names: dict[str, str] | None = None,
    task: str | None = None, condition: str | None = None,
) -> RunDescription:
    """Describe one working directory, reading no result file.

    ``names`` supplements the folder's own ``names.map`` and wins where both
    have an id: RIFLEX writes the map only in the dynmod folder, and it is
    task-level, so a static run can borrow a sibling's.

    ``task`` and ``condition`` override what the folder says about itself, which
    is, nearest first: ``results.json``, the ``variables.inp`` header, and the
    folder path.
    """
    path = Path(folder).absolute()
    return _describe(path, _entries(path), names, task, condition)


def _describe(path: Path, entries: tuple[Entry, ...], names: dict[str, str] | None,
              task: str | None, condition: str | None) -> RunDescription:
    manifests = list(_manifests(path))
    declared_task, variables = read_variables(path)
    from_manifest = _variables_for(manifests, path.name, is_member(path))
    if from_manifest is not None:
        variables = from_manifest
    named_task, named_condition = _run_of(manifests)
    found_task, found_condition = _identify(path)
    # results.json names the condition a set member belongs to, a level up; the
    # member's tree is named by its own folder.
    own_name = found_condition if is_member(path) else (named_condition or found_condition)
    return RunDescription(
        task=task or named_task or declared_task or found_task,
        condition=condition or own_name,
        entries=entries,
        variables=variables,
        names={**read_names(path), **(names or {})},
    )


def describe_condition(
    folder: str | Path, *, names: dict[str, str] | None = None,
    task: str | None = None, condition: str | None = None,
) -> RunDescription | None:
    """Describe a condition from the ``results.json`` in its root, or None without one.

    ``directories`` names the working directory of each analysis, so a static and
    a dynamic run in separate timestamp folders become one run again, and stale
    folders are never read. A set gets one member description each, as SIMA's
    post processor shows them. Without directories there is nothing to follow.
    """
    root = Path(folder).absolute()
    content = _read_manifest(root / RESULTS_FILENAME)
    if content is None:
        return None
    named_task, named_condition = _run_of([content])
    found_task, found_condition = _identify(root)
    task = task or named_task or found_task
    condition = condition or named_condition or found_condition
    members = content.get("conditions")
    if isinstance(members, list):
        described = [_member(root, entry, task, names) for entry in members if isinstance(entry, dict)]
        if not described or any(member is None for member in described):
            return None
        return RunDescription(
            task=task, condition=condition,
            variables=_variables_of(content.get("variables")),
            names={key: value for member in described for key, value in member.names.items()},
            members=tuple(described),
        )
    directories = _directories_of(content.get("directories"))
    if not directories:
        return None
    entries, found_names = _entries_in(root, directories)
    return RunDescription(
        task=task, condition=condition, entries=entries,
        variables=_variables_of(content.get("variables")),
        names={**found_names, **(names or {})},
    )


def _member(root: Path, entry: dict, task: str,
            names: dict[str, str] | None) -> RunDescription | None:
    directories = _directories_of(entry.get("directories"))
    condition = entry.get("condition")
    if not directories or not isinstance(condition, str):
        return None
    entries, found_names = _entries_in(root, directories)
    return RunDescription(
        task=task, condition=condition, entries=entries,
        variables=_variables_of(entry.get("variables")),
        names={**found_names, **(names or {})},
    )


def _directories_of(value: object) -> dict[str, str]:
    if not isinstance(value, dict):
        return {}
    return {name: path for name, path in value.items()
            if isinstance(name, str) and isinstance(path, str)}


def _entries_in(root: Path, directories: dict[str, str]) -> tuple[tuple[Entry, ...], dict[str, str]]:
    """Each analysis read from its own directory, with paths relative to ``root``.

    A directory contributes only the files of its analysis: SIMA copies static
    results such as ``psc.lis`` into the dynamic folder too. Files whose name
    names no analysis are read once per directory.
    """
    grouped: dict[str, list[ResultFile]] = {name: [] for name in directories}
    run_types: dict[str, str] = {}
    unmatched: list[ResultFile] = []
    names: dict[str, str] = {}
    seen: set[Path] = set()
    for name, relative in directories.items():
        folder = (root / relative).resolve()
        if not folder.is_dir():
            continue
        first_visit = folder not in seen
        seen.add(folder)
        if first_visit:
            names.update(read_names(folder))
        for child in sorted(folder.iterdir()):
            if not is_result(child):
                continue
            result = ResultFile(file=f"{relative.rstrip('/')}/{child.name}" if relative != "." else child.name)
            phase = phase_of(child.name)
            if phase is None:
                if first_visit:
                    unmatched.append(result)
            elif phase[0] == name:
                grouped[name].append(result)
                run_types[name] = phase[1]
    ordered = sorted(grouped, key=lambda name: (_ENTRY_ORDER.index(name) if name in _ENTRY_ORDER
                                                else len(_ENTRY_ORDER)))
    entries = [Entry(name=name, run_type=run_types.get(name), results=_in_sima_order(grouped[name]))
               for name in ordered if grouped[name]]
    if unmatched:
        entries.append(Entry(name="", container=False, results=tuple(unmatched)))
    return tuple(entries), names
