"""Reader dispatch, by file extension as SIMA's folder import does, or by exact name."""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar, Protocol, TypeVar

from ._node import Container
from ._sources import Source


class Reader(Protocol):  # pylint: disable=too-few-public-methods
    """Fills a container from one result file."""

    #: Lowercase file extensions, without the dot, this reader handles.
    types: ClassVar[frozenset[str]]

    #: Lowercase file names this reader handles, checked before the extension.
    #: For a format whose extension other files share: ``psc.lis`` but not ``prs.lis``.
    names: ClassVar[frozenset[str]] = frozenset()

    def read(self, source: Source, into: Container) -> None:
        """Fill ``into`` with what ``source`` contains.

        ``into`` is always freshly created and empty -- never inspect it. That
        is what makes the import order-independent.
        """


_REGISTRY: dict[str, Reader] = {}
_BY_NAME: dict[str, Reader] = {}

R = TypeVar("R", bound=type)


def register(reader_class: R) -> R:
    """Register a reader class for every extension and name it declares. Used as a decorator."""
    instance = reader_class()
    for type_name in reader_class.types:
        _REGISTRY[type_name] = instance
    for name in getattr(reader_class, "names", ()):
        _BY_NAME[name] = instance
    return reader_class


def find_reader(path: Path) -> Reader | None:
    """The reader for a file, or None if no reader claims its name or extension."""
    by_name = _BY_NAME.get(path.name.lower())
    if by_name is not None:
        return by_name
    extension = extension_of(path)
    return _REGISTRY.get(extension) if extension else None


def extension_of(path: Path) -> str | None:
    """The lowercase extension without its dot."""
    suffix = path.suffix
    return suffix[1:].lower() if len(suffix) > 1 else None
