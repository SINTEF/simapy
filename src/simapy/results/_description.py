"""What one run folder holds, as the tree builder needs it.

Kept apart from :mod:`simapy.results._scan` so that the importer depends on the
shape of a run and not on how that shape was arrived at.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Mapping


class ResultsError(Exception):
    """A folder or file cannot be read at all.

    Not for a file inside a folder that could not be read -- that is best effort
    and lands in :class:`~simapy.results.SourceReport` instead.
    """


@dataclass(frozen=True)
class ResultFile:
    """One file to hand to a reader, which its extension selects."""

    file: str


@dataclass(frozen=True)
class Variable:
    """One condition variable and its unit, if it has one."""

    value: object
    unit: str | None = None

    def __str__(self) -> str:
        return f"{self.value} [{self.unit}]" if self.unit else str(self.value)


@dataclass(frozen=True)
class Entry:
    """One analysis phase, and the files that belong to it."""

    name: str
    run_type: str | None = None
    #: False grafts the files straight onto the condition: their name does not
    #: say which analysis produced them, so they go one level up, not under a guess.
    container: bool = True
    results: tuple[ResultFile, ...] = ()


@dataclass(frozen=True)
class RunDescription:
    """One condition's run: what to read, and the little that names it.

    For a condition set, ``members`` holds one description per member, and
    ``variables`` the ones the set holds constant.
    """

    task: str
    condition: str
    entries: tuple[Entry, ...] = ()
    variables: Mapping[str, Variable] = field(default_factory=dict)
    #: ``names.map`` folded in, so no reader resolves hashed model ids itself.
    names: Mapping[str, str] = field(default_factory=dict)
    members: tuple[RunDescription, ...] = ()

    def __post_init__(self):
        object.__setattr__(self, "variables", MappingProxyType(dict(self.variables)))
        object.__setattr__(self, "names", MappingProxyType(dict(self.names)))
