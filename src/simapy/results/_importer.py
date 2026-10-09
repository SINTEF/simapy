"""Run description to signal tree.

The shape of the tree, the graft-or-flatten rule, the copy-then-merge contract
and the error handling all follow SIMA; what differs is where the metadata comes
from -- the run folder rather than the model.

A condition set is task, set, then one condition per member -- the tree SIMA's
post processor shows -- and needs a description of every member, which only the
set's ``results.json`` gives.
"""

from __future__ import annotations

from pathlib import Path
from typing import Mapping

from ._description import Entry, ResultFile, RunDescription, Variable
from ._build import (
    add_signal,
    get_or_create_child,
    graft,
    insert_child,
    prune_empty,
    set_attribute,
    set_type,
    shallow_copy,
)
from ._merge import merge_containers
from ._node import Container, ErrorSignal, Signal, constant
from ._registry import extension_of, find_reader
from ._sources import FolderContext, Source, SourceError, SourceReport, Status, warn

TYPE_TASK = "task"
TYPE_CONDITION = "condition"
#: The set's own type, and the attribute naming the set (or, alone, the condition) a run belongs to.
TYPE_CONDITION_CONTAINER = "conditionContainer"
#: Named "Variables" and inserted first, as SIMA does.
VARIABLES = "Variables"
TYPE_VARIABLES = "variables"
TYPE_VARIABLE = "variable"


def build_tree(
    description: RunDescription, folder: Path
) -> tuple[Container, list[SourceReport]]:
    """Build the tree for one working directory, and report on every file."""
    context = FolderContext(folder=folder, names=dict(description.names))
    reports: list[SourceReport] = []

    task = Container(description.task, type=TYPE_TASK)
    condition = Container(description.condition, type=TYPE_CONDITION,
                          **{TYPE_CONDITION_CONTAINER: description.condition})
    graft(task, condition)

    for entry in description.entries:
        _add_entry(condition, entry, context, reports)

    prune_empty(condition)
    # After pruning, as createAndAddResultsFromSingleCondition does -- otherwise
    # a run whose only content is its variables would prune itself away.
    _add_variables(condition, description.variables)

    reports.extend(
        SourceReport(unread.file, extension_of(Path(unread.file)) or "", Status.UNSUPPORTED,
                     detail=unread.advice)
        for unread in description.unread
    )
    return task, reports


def build_set_tree(
    description: RunDescription, folder: Path
) -> tuple[Container, list[SourceReport]]:
    """Build a condition set's tree: ``createAndAddResultsFromSimpleConditionProvider``."""
    task = Container(description.task, type=TYPE_TASK)
    conditions = Container(description.condition, type=TYPE_CONDITION_CONTAINER)
    graft(task, conditions)
    _add_variables(conditions, description.variables)
    reports: list[SourceReport] = []
    for member in description.members:
        member_root, member_reports = build_tree(member, folder)
        condition = member_root.containers[0]
        set_attribute(condition, TYPE_CONDITION_CONTAINER, description.condition)
        graft(conditions, condition)
        reports.extend(member_reports)
    return task, reports


def _add_variables(condition: Container, variables: Mapping[str, Variable]) -> None:
    """One constant signal per variable, typed ``variable``, unit ``-`` when it has none.

    The container goes in at index 0, as SIMA puts it, ahead of the results.
    """
    if not variables:
        return
    container = Container(VARIABLES, type=TYPE_VARIABLES)
    for name, variable in variables.items():
        signal = constant(name, variable.value, type=TYPE_VARIABLE)
        set_attribute(signal, "unit", variable.unit or "-")
        add_signal(container, signal)
    insert_child(condition, 0, container)


def _add_entry(
    condition: Container,
    entry: Entry,
    context: FolderContext,
    reports: list[SourceReport],
) -> None:
    """Graft or flatten one analysis, then read its files into it."""
    if entry.container:
        target = get_or_create_child(condition, entry.name)
        # Only if unset, matching getOrCreateChild + the null check on type.
        if target.type is None and entry.run_type:
            set_type(target, entry.run_type)
    else:
        target = condition

    for result in entry.results:
        reports.append(_add_data(target, result, context))


def _add_data(
    container: Container, result: ResultFile, context: FolderContext
) -> SourceReport:
    """Read one result file into ``container``.

    The reader is handed a fresh shallow copy and can never observe what other
    readers produced, so the import is order-independent.
    """
    path = context.folder / result.file
    kind = extension_of(path) or ""

    if not path.is_file():
        detail = "gone between listing the folder and reading it"
        warn(f"{result.file}: {detail}")
        return SourceReport(result.file, kind, Status.MISSING, detail=detail)

    proxy = shallow_copy(container)
    try:
        reader = find_reader(path)
        if reader is None:
            raise SourceError(f"no reader for extension {path.suffix!r}")
        reader.read(Source(path=path, context=context), proxy)
    except Exception as exc:  # readers may raise anything a parser raises
        error = SourceError(f"Unable to import result {path}: {exc}")
        error.__cause__ = exc
        add_signal(container, ErrorSignal(f"Unable to import result {result.file}", error))
        detail = f"{type(exc).__name__}: {exc}"
        warn(f"{result.file}: {detail}")
        return SourceReport(result.file, kind, Status.FAILED, detail=detail)

    signals = sum(1 for node in proxy.walk() if isinstance(node, Signal))
    merge_containers(container, proxy)
    return SourceReport(result.file, kind, Status.READ, signals=signals)
