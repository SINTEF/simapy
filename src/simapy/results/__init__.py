"""Read SIMA results as a lazy signal hierarchy.

    >>> from simapy.results import open_results
    >>> res = open_results(condition_folder)
    >>> res.run.signal("Static/RiserLine/Static forces/EFF. TENSION").unit
    'N'

The tree matches the one SIMA builds -- same containers, types and merge rules
-- because the code that builds it is a port of SIMA's own importer.

Reading is best effort. Opening a folder never raises because one result file is
unreadable: the failure lands in :attr:`ResultSet.sources` and as an
:class:`ErrorSignal` in the tree, where the data should have been.
"""

from __future__ import annotations

from pathlib import Path

from . import _readers  # noqa: F401  -- registers the readers
from . import _scan
from ._build import adopt as _adopt
from ._build import rename_duplicates as _rename_duplicates
from ._description import ResultsError, RunDescription, Variable
from ._frames import signals_to_frame
from ._importer import build_set_tree, build_tree
from ._node import Container, ErrorSignal, Node, Signal
from ._sources import SourceError, SourceReport, Status

#: Everything this package promises; the modules behind it are implementation.
__all__ = [
    "open_results",
    "ResultSet",
    "Container",
    "Signal",
    "ErrorSignal",
    "Node",
    "RunDescription",
    "Variable",
    "ResultsError",
    "SourceError",
    "SourceReport",
    "Status",
    "signals_to_frame",
]


class ResultSet(Container):
    """The tree read from a folder or a file, plus what was read to build it."""

    def __init__(
        self, root: Container, folder: Path, description: RunDescription, sources
    ):
        super().__init__(root.name)
        _adopt(self, root)
        _rename_duplicates([self])
        self._folder = folder
        self._description = description
        self._sources: tuple[SourceReport, ...] = tuple(sources)

    @property
    def folder(self) -> Path:
        return self._folder

    @property
    def description(self) -> RunDescription:
        return self._description

    @property
    def sources(self) -> tuple[SourceReport, ...]:
        """One :class:`SourceReport` per result file the folder offered."""
        return self._sources

    @property
    def run(self) -> Container:
        """The condition's container, or for a set the set's: every result read sits below it."""
        return self.container(self._description.condition)

    def __repr__(self) -> str:
        read = sum(1 for s in self._sources if s.status is Status.READ)
        return (
            f"<ResultSet {self.name!r} {self._description.condition!r} "
            f"sources={read}/{len(self._sources)} read>"
        )


def open_results(
    source: str | Path, *, names: dict[str, str] | None = None,
    task: str | None = None, condition: str | None = None,
) -> ResultSet:
    """Open a condition folder, one working directory, or one result file.

    A condition folder is read as the ``results.json`` SIMA 5.4 and later
    writes there describes it: each analysis from its own working directory,
    and a set as one condition per member. A working directory reads every
    result in it. A file reads that file alone, which is how a workflow's
    output is opened.

    Only the folder listing and each file's structure are read here -- names,
    types, units and ``len()``. Values are read when ``.x`` or ``.y`` is
    touched; JSON, which has to be parsed whole, is the exception.

    :param names: hashed model id to name, overriding what the folder gives.
    :param task: overrides the task name the folder gives.
    :param condition: overrides the condition name the folder gives.
    :raises ResultsError: if ``source`` is neither a directory nor a file, is a
        file no reader claims, or is a folder with no result to read. A result
        file that fails to read is not an error: it shows in
        :attr:`ResultSet.sources`.
    """
    path = Path(source).absolute()
    if path.is_file():
        description = _scan.describe_file(path, names=names, task=task, condition=condition)
        root, reports = build_tree(description, path.parent)
        return ResultSet(root, path.parent, description, reports)
    if not path.is_dir():
        raise ResultsError(f"{path} is not a directory or a file")

    whole = _scan.describe_condition(path, names=names, task=task, condition=condition)
    if whole is not None:
        build = build_set_tree if whole.members else build_tree
        root, reports = build(whole, path)
        return ResultSet(root, path, whole, reports)

    description = _scan.describe(path, names=names, task=task, condition=condition)
    if not description.entries:
        runs = ", ".join(run.relative_to(path).as_posix() for run in _scan.find_runs(path))
        hint = f"; open one of its runs: {runs}" if runs else ""
        raise ResultsError(f"{path} holds no result files{hint}")
    root, reports = build_tree(description, path)
    return ResultSet(root, path, description, reports)
