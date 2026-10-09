"""What a reader is handed, and what it reports back."""

from __future__ import annotations

import os
import re
import sys
import warnings
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

_PACKAGE = str(Path(__file__).parent) + os.sep


class SourceError(Exception):
    """A registered result file could not be read."""


class Status(Enum):
    """What became of one result file."""

    READ = "read"
    FAILED = "failed"
    #: Gone between listing the folder and reading it.
    MISSING = "missing"
    #: A storage format SIMA still writes but no reader here reads.
    UNSUPPORTED = "unsupported"


class UnsupportedStorageWarning(UserWarning):
    """Results were skipped because SIMA stored them in a format simapy does not read."""


def warn(message: str, category: type[Warning] = UserWarning) -> None:
    """Warn at the first caller outside this package, wherever inside it the warning arose."""
    level = 2
    frame = sys._getframe(1)  # pylint: disable=protected-access
    while frame is not None and frame.f_code.co_filename.startswith(_PACKAGE):
        frame = frame.f_back
        level += 1
    warnings.warn(message, category, stacklevel=level)


@dataclass
class FolderContext:
    """Run-folder knowledge shared by every reader.

    Result files are not self-contained: an ``.mpf`` identifies lines by hashed
    id (``line Risea63d``) and cannot resolve them alone.
    """

    folder: Path
    #: Hashed id to model name, from ``names.map`` in this folder.
    names: dict[str, str] = field(default_factory=dict)

    def resolve_names(self, text: str) -> str:
        """Replace every known short id embedded in ``text``.

        Substring replacement, because an mpf carries ids inside prose:
        ``"Static forces, line Moor1e20 / step 10"``. One pass, so a replaced
        name is never rewritten again by an id it happens to contain.
        """
        if not self.names:
            return text
        return _id_pattern(tuple(self.names)).sub(lambda m: self.names[m.group(0)], text)

    def resolve_id(self, name: str) -> str:
        """Resolve a name expected to be an id on its own.

        Exact lookup: an HDF5 group name is an id or a real name, never prose,
        and a substring rule could corrupt a real name that contains an id.
        """
        return self.names.get(name, name)


_PATTERNS: dict[tuple[str, ...], re.Pattern[str]] = {}


def _id_pattern(ids: tuple[str, ...]) -> re.Pattern[str]:
    pattern = _PATTERNS.get(ids)
    if pattern is None:
        alternatives = sorted(ids, key=len, reverse=True)
        pattern = _PATTERNS[ids] = re.compile("|".join(map(re.escape, alternatives)))
    return pattern


@dataclass(frozen=True)
class Source:
    """One result file, with the context needed to read it."""

    path: Path
    context: FolderContext

    @property
    def file(self) -> str:
        """The file name, without its directory."""
        return self.path.name


@dataclass(frozen=True)
class SourceReport:
    """The outcome of one result file. Collected on ``ResultSet.sources``."""

    file: str
    type: str
    status: Status
    signals: int = 0
    detail: str | None = None

    def __str__(self) -> str:
        if self.status is Status.READ:
            return f"read ({self.signals} signals)"
        return f"{self.status.value}: {self.detail}"

    def __repr__(self) -> str:
        return f"<{self.file} {self.type} {self}>"
