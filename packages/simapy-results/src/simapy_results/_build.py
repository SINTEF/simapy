"""Filling the tree: the write half of :class:`~simapy_results.Container`.

Kept out of the class so that what ``open_results`` returns cannot be altered by
the code reading it, and how a tree is filled stays free to change.
"""

from __future__ import annotations

# pylint: disable=protected-access  # no friend declaration in Python

from ._node import DUPLICATE, TYPE, Container, Node, Signal


def graft(parent: Container, child: Container) -> Container:
    """Append ``child`` to ``parent``."""
    child._parent = parent
    parent._containers.append(child)
    return child


def insert_child(parent: Container, index: int, child: Container) -> Container:
    """Place ``child`` at a fixed position among ``parent``'s containers."""
    child._parent = parent
    parent._containers.insert(index, child)
    return child


def add_signal(parent: Container, signal: Signal) -> Signal:
    """Append ``signal`` to ``parent``."""
    signal._parent = parent
    parent._signals.append(signal)
    return signal


def get_or_create_child(parent: Container, name: str) -> Container:
    """The child of ``parent`` called ``name``, created empty if absent."""
    child = next((c for c in parent._containers if c.name == name), None)
    if child is None:
        child = graft(parent, Container(name))
    return child


def replace_containers(parent: Container, containers: list[Container]) -> None:
    """Swap in a new child list, reparenting every member."""
    parent._containers = list(containers)
    for child in parent._containers:
        child._parent = parent


def adopt(parent: Container, source: Container) -> None:
    """Take over ``source``'s containers and signals, attributes included."""
    parent._attributes = dict(source._attributes)
    replace_containers(parent, source._containers)
    parent._signals = list(source._signals)
    for signal in parent._signals:
        signal._parent = parent


def set_type(node: Node, value: str) -> None:
    """Set the node type."""
    node._attributes[TYPE] = value


def set_attribute(node: Node, key: str, value: str) -> None:
    """Set one free-form attribute."""
    node._attributes[key] = value


def update_attributes(node: Node, attributes: dict[str, str]) -> None:
    """Set several free-form attributes at once."""
    node._attributes.update(attributes)


def clear_signals(container: Container) -> None:
    """Drop every signal, keeping the containers."""
    container._signals.clear()


def rename(node: Node, name: str) -> None:
    """Rename a node, as a reader does once an id map resolves its short id."""
    node._name = name


def rename_duplicates(items: list[Node]) -> None:
    """``SignalItemUtil.renameDuplicates``: later same-named siblings become ``name_duplicate_N``.

    As in SIMA, a renamed container is not itself searched.
    """
    renamed: set[int] = set()
    for i, first in enumerate(items):
        if i in renamed:
            continue
        count = 0
        for j in range(i + 1, len(items)):
            if items[j]._name == first._name:
                count += 1
                items[j]._name = f"{items[j]._name}{DUPLICATE}{count}"
                renamed.add(j)
        if isinstance(first, Container):
            rename_duplicates([*first._containers, *first._signals])


def merge_attributes(node: Node, other: Node) -> None:
    """Fold ``other``'s attributes into ``node``, keeping what ``node`` already set."""
    for key, value in other._attributes.items():
        node._attributes.setdefault(key, value)


def shallow_copy(container: Container) -> Container:
    """Same name, type and attributes; no containers, no signals.

    Every reader is handed one of these, so readers can never observe each
    other's output.
    """
    clone = Container(container.name)
    clone._attributes = dict(container._attributes)
    return clone


def prune_empty(container: Container) -> None:
    """Drop containers with no containers and no signals, bottom-up."""
    for child in container._containers:
        prune_empty(child)
    container._containers = [c for c in container._containers if len(c) > 0]
