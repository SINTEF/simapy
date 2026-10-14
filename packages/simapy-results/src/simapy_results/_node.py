"""The signal hierarchy.

A node has a name, a type, free-form string attributes and a parent; a
container has containers and signals -- the shape SIMA gives its own signals.

Deliberately independent of ``dmtpy``, but the vocabulary (``type``, ``unit``,
``xunit`` and the type strings) is kept identical, so converting a subtree into
the DMT signals model stays mechanical.
"""

from __future__ import annotations

import collections.abc
import re
from functools import lru_cache
from types import MappingProxyType
from typing import TYPE_CHECKING, Any, Iterable, Iterator, Mapping, Protocol

import numpy as np

from ._units import conversion_factor

if TYPE_CHECKING:
    from ._sources import SourceError

#: Attribute key holding the node type.
TYPE = "type"

#: Attribute key used to order siblings of equal type.
INDEX = "index"

#: The requirement key SIMA matches against a node's dotted path.
PATH = "path"

PATH_SEPARATOR = "/"

#: SIMA's ``getPath()`` separator, used only by :meth:`Container.select`.
SIMA_SEPARATOR = "."

#: SIMA's suffix for the second and later sibling sharing a name.
DUPLICATE = "_duplicate_"


class Node:
    """Base of the hierarchy. Read-only."""

    def __init__(self, name: str = "", type: str | None = None, **attributes: str):
        self._name = name
        self._attributes: dict[str, str] = dict(attributes)
        self._parent: Container | None = None
        if type is not None:
            self._attributes[TYPE] = type

    @property
    def name(self) -> str:
        return self._name

    @property
    def attributes(self) -> Mapping[str, str]:
        return MappingProxyType(self._attributes)

    @property
    def parent(self) -> Container | None:
        return self._parent

    @property
    def type(self) -> str | None:
        return self._attributes.get(TYPE)

    @property
    def path(self) -> str:
        """Slash-separated path from the root, excluding the root's own name."""
        return PATH_SEPARATOR.join(self._names()[1:])

    def _names(self) -> list[str]:
        """Names from the root down to this node, the root's own first."""
        names: list[str] = []
        node: Node | None = self
        while node is not None:
            names.append(node.name)
            node = node.parent
        return names[::-1]

    def __repr__(self) -> str:
        kind = self.type or self.__class__.__name__.lower()
        return f"<{self.__class__.__name__} {self.name!r} type={kind!r}>"


class Container(Node):
    """A node with containers and signals, read like a mapping from key to node.

    The read-only result tree, not the DMT model class ``simapy.sima.signals.Container``.
    """

    def __init__(self, name: str = "", type: str | None = None, **attributes: str):
        super().__init__(name, type, **attributes)
        self._containers: list[Container] = []
        self._signals: list[Signal] = []

    @property
    def containers(self) -> tuple[Container, ...]:
        return tuple(self._containers)

    @property
    def signals(self) -> tuple[Signal, ...]:
        return tuple(self._signals)

    def keys(self) -> list[str]:
        return [key for key, _ in self._entries()]

    def values(self) -> list[Node]:
        return [node for _, node in self._entries()]

    def items(self) -> list[tuple[str, Node]]:
        return self._entries()

    def get(self, key: str, default: Container | Signal | None = None) -> Container | Signal | None:
        try:
            return self[key]
        except KeyError:
            return default

    def _entries(self) -> list[tuple[str, Node]]:
        """Children then signals, by name."""
        return [(node.name, node) for node in (*self._containers, *self._signals)]

    def _get_child(self, name: str) -> Container | None:
        return next((child for child in self._containers if child.name == name), None)

    def _get_signal(self, name: str) -> Signal | None:
        return next((signal for signal in self._signals if signal.name == name), None)

    # pylint: disable=protected-access  # _get_child / _get_signal on a sibling node

    def _walk_to(self, key: str) -> tuple[Container, str]:
        """The container holding the last segment of ``key``, and that segment.

        A name may itself contain ``/``, so each step takes the longest child
        name the remaining path starts with rather than splitting on every ``/``.
        """
        if not all(key.split(PATH_SEPARATOR)):
            raise KeyError(f"{key!r} is not a valid name or path")

        parent: Container = self
        rest = key
        while PATH_SEPARATOR in rest and not parent._holds(rest):
            prefixes = [
                (entry, node) for entry, node in parent._entries()
                if isinstance(node, Container) and rest.startswith(entry + PATH_SEPARATOR)
            ]
            if not prefixes:
                raise KeyError(_not_found(parent, rest.split(PATH_SEPARATOR, 1)[0]))
            entry, parent = max(prefixes, key=lambda pair: len(pair[0]))
            rest = rest[len(entry) + 1:]
        return parent, rest

    def _holds(self, name: str) -> bool:
        return self._get_child(name) is not None or self._get_signal(name) is not None

    def __getitem__(self, key: str) -> Container | Signal:
        """Look up a child or signal by name, or a ``a/b/c`` path.

        A container wins over a same-named signal; :meth:`signal` and
        :meth:`container` say which one is meant.
        """
        parent, last = self._walk_to(key)
        # Explicit None checks: an empty container is falsy, so `a or b` would
        # skip a childless child and report it missing.
        child = parent._get_child(last)
        found: Container | Signal | None = child if child is not None else parent._get_signal(last)
        if found is None:
            raise KeyError(_not_found(parent, last))
        return found

    def signal(self, key: str) -> Signal:
        """Look up a signal by name or path.

        Searches signals only, so a same-named container does not shadow the
        signal the caller asked for.
        """
        parent, last = self._walk_to(key)
        found = parent._get_signal(last)
        if found is None:
            if parent._get_child(last) is not None:
                raise TypeError(f"{key!r} is a container, not a signal")
            raise KeyError(_not_found(parent, last))
        return found

    def container(self, key: str) -> Container:
        """Look up a child container by name or path."""
        parent, last = self._walk_to(key)
        found = parent._get_child(last)
        if found is None:
            if parent._get_signal(last) is not None:
                raise TypeError(f"{key!r} is a signal, not a container")
            raise KeyError(_not_found(parent, last))
        return found

    def __contains__(self, key: object) -> bool:
        if not isinstance(key, str):
            return False
        try:
            self[key]
        except KeyError:
            return False
        return True

    def __iter__(self) -> Iterator[str]:
        # Without this, __getitem__ makes Container look like a legacy sequence
        # and `list(c)` indexes it with integers.
        return iter(self.keys())

    def __len__(self) -> int:
        return len(self._containers) + len(self._signals)

    # -- traversal -------------------------------------------------------

    def walk(self) -> Iterator[Node]:
        """Depth-first over every descendant, containers before their signals."""
        for child in self._containers:
            yield child
            yield from child.walk()
        yield from self._signals

    def find(self, **query: str) -> list[Node]:
        """Every descendant whose attributes match.

        ``name`` is matched against the node name rather than an attribute.
        """
        return [node for node in self.walk() if _matches(node, query)]

    def _paths(self, prefix: str = "") -> Iterator[tuple[str, Node]]:
        """Every descendant with its key path relative to this container."""
        for key, node in self._entries():
            yield prefix + key, node
            if isinstance(node, Container):
                yield from node._paths(prefix + key + PATH_SEPARATOR)

    def select(self, *paths: str, **requirements: str | Iterable[str]) -> dict[str, Signal]:
        """Signals meeting SIMA's signal requirements, keyed by path.

        The rules are SIMA's own (``SignalItemQuery``), so a requirement copied
        from SIMA selects the same signals here:

        * each keyword is an ``attribute=value`` requirement, and positional
          arguments are ``path`` requirements. Values of one key are alternatives,
          different keys must all hold; no requirement selects everything;
        * ``path`` is SIMA's dotted path from the root, the task's name first --
          ``Task.Initial.Dynamic.RiserLine.Force envelope curve.F-MAX``. Without
          a ``*`` it names a node exactly, and naming a container selects its
          subtree;
        * ``*`` matches anything, across levels too, ``?`` at most one character,
          and ``.``, ``(`` and ``)`` are literal;
        * a container meeting every requirement brings all its signals.

        Keys are relative to this container and go straight back into ``[]``.

            >>> res.select("*.Dynamic.*.F-MAX")  # doctest: +SKIP
            >>> res.select(name=["XG translation", "YG translation"])  # doctest: +SKIP
        """
        wanted = _requirements(paths, requirements)
        chain = tuple(_dotted(self._names()))
        if _meets(self, wanted, chain):
            return {path: node for path, node in self._paths() if isinstance(node, Signal)}
        found: dict[str, Signal] = {}
        self._collect(wanted, "", chain, found)
        return found

    def _collect(self, wanted: dict[str, list[str]], prefix: str,
                 chain: tuple[str, ...], found: dict[str, Signal]) -> None:
        for key, node in self._entries():
            path = prefix + key
            node_chain = (*chain, chain[-1] + SIMA_SEPARATOR + key)
            if isinstance(node, Container):
                if _meets(node, wanted, node_chain):
                    found.update(
                        (sub, signal) for sub, signal in node._paths(path + PATH_SEPARATOR)
                        if isinstance(signal, Signal)
                    )
                else:
                    node._collect(wanted, path + PATH_SEPARATOR, node_chain, found)
            elif _meets(node, wanted, node_chain):
                found[path] = node

    def to_dataframe(self, recursive: bool = False, index: bool = True):
        """This container's signals as a pandas DataFrame. Requires pandas.

        See :func:`~simapy_results.signals_to_frame`.
        """
        from ._frames import container_to_frame  # pylint: disable=import-outside-toplevel

        return container_to_frame(self, recursive, index)


# Registered rather than inherited: Mapping's __eq__ would compare trees by
# content and make every node unhashable.
collections.abc.Mapping.register(Container)


def _matches(node: Node, query: dict[str, str]) -> bool:
    """True when every queried attribute is present with the given value."""
    for key, value in query.items():
        if key == "name":
            if node.name != value:
                return False
        elif node.attributes.get(key) != value:
            return False
    return True


def _requirements(paths: tuple[str, ...], requirements: dict[str, Any]) -> dict[str, list[str]]:
    wanted: dict[str, list[str]] = {}
    for key, value in (*((PATH, path) for path in paths), *requirements.items()):
        values = [value] if isinstance(value, str) or not isinstance(value, Iterable) else value
        wanted.setdefault(key, []).extend(str(v) for v in values)
    return wanted


def _dotted(keys: list[str]) -> Iterator[str]:
    """The SIMA path of each node along ``keys``, the root's first."""
    path = ""
    for index, key in enumerate(keys):
        path = key if index == 0 else path + SIMA_SEPARATOR + key
        yield path


def _meets(node: Node, wanted: dict[str, list[str]], chain: tuple[str, ...]) -> bool:
    return all(
        any(_meets_one(node, key, value, chain) for value in values)
        for key, values in wanted.items()
    )


def _meets_one(node: Node, key: str, value: str, chain: tuple[str, ...]) -> bool:
    """SIMA's ``SingleRequirementMatcher``; ``chain`` is the node's path and its ancestors'."""
    if key == PATH and isinstance(node, Signal):
        if not value.endswith("*"):
            if value in chain:
                return True
            if "*" not in value:
                return False
        return _wildcard(chain[-1], value)
    actual = node.name if key == "name" else node.attributes.get(key)
    if actual is None and key == PATH:
        actual = chain[-1]
    return actual is not None and _wildcard(actual, value)


#: What sends SIMA's ``Matcher`` to a regular expression, along with a third ``*``.
_REGEX_TRIGGERS = frozenset(".?()")


def _wildcard(value: str, requirement: str) -> bool:
    """SIMA's ``Matcher.matches``: literal text with up to two ``*``, else a regex.

    In the literal form every other character means itself, so ``X+*`` only
    matches names starting ``X+``. SIMA's two-star test lets the middle part
    overlap the end (``a*c*c`` matches ``ac``); that overlap is not reproduced.
    """
    if _REGEX_TRIGGERS.intersection(requirement) or requirement.count("*") > 2:
        return _pattern(requirement).fullmatch(value) is not None
    if "*" not in requirement:
        return value == requirement
    head, *middle, tail = requirement.split("*")
    if len(value) < len(head) + len(tail) or not value.startswith(head) or not value.endswith(tail):
        return False
    inner = value[len(head):len(value) - len(tail)]
    return all(part in inner for part in middle)


@lru_cache(maxsize=256)
def _pattern(requirement: str) -> re.Pattern[str]:
    """SIMA's ``escapeSpecialCharacters``; any other character stays regex, as there."""
    escaped = {".": "[.]", "*": ".*", "?": ".?", "(": r"\(", ")": r"\)"}
    try:
        return re.compile("".join(escaped.get(char, char) for char in requirement))
    except re.error as error:
        raise ValueError(f"invalid requirement {requirement!r}: {error}") from error


def _not_found(parent: Container, part: str) -> str:
    if parent._get_signal(part) is not None:  # pylint: disable=protected-access
        return f"{part!r} is a signal and has no members"
    return f"{part!r} not found in {parent.name!r}; available: {parent.keys()}"


class Values(Protocol):
    """Deferred access to one signal's numbers.

    A provider whose x-axis is equidistant sets ``xstart`` and ``xdelta`` and
    never stores an x array, as SIMA does: a stored time axis per signal would
    cost as much memory as the values themselves.
    """

    @property
    def size(self) -> int:
        """Sample count. Must not read values."""

    def x(self) -> np.ndarray: ...

    def y(self) -> np.ndarray: ...


class Equidistant:
    """Values on an implied x-axis: ``xstart + i * xdelta``.

    ``x()`` builds an array each call rather than caching one, so a signal never
    holds an x-axis it was only asked for once. Callers that need it repeatedly
    should keep the result -- or use a DataFrame, which builds one index for a
    whole set of signals sharing an axis.
    """

    def __init__(self, size: int, xstart: float, xdelta: float):
        self._size = size
        self.xstart = xstart
        self.xdelta = xdelta

    @property
    def size(self) -> int:
        return self._size

    def x(self) -> np.ndarray:
        return self.xstart + np.arange(self._size, dtype=np.float64) * self.xdelta

    def y(self) -> np.ndarray:
        raise NotImplementedError


class Signal(Node):
    """A named series."""

    # pylint: disable=missing-function-docstring  # unit/xunit/x/y are self-describing

    def __init__(
        self,
        name: str,
        values: Values,
        unit: str | None = None,
        xunit: str | None = None,
        **attributes: str,
    ):
        super().__init__(name, **attributes)
        self._values = values
        if unit is not None:
            self._attributes["unit"] = unit
        if xunit is not None:
            self._attributes["xunit"] = xunit

    @property
    def unit(self) -> str | None:
        return self.attributes.get("unit")

    @property
    def xunit(self) -> str | None:
        return self.attributes.get("xunit")

    @property
    def is_equidistant(self) -> bool:
        """True when the x-axis is implied by ``xstart`` and ``xdelta``."""
        return self.xdelta is not None

    @property
    def xstart(self) -> float | None:
        """First x value, if the axis is equidistant."""
        return getattr(self._values, "xstart", None)

    @property
    def xdelta(self) -> float | None:
        """Spacing between x values, if the axis is equidistant."""
        return getattr(self._values, "xdelta", None)

    def same_axis(self, other: Signal) -> bool:
        """Whether two signals share an x-axis, without materialising either.

        Equidistant signals compare on start, delta and size -- which is free.
        Anything else has to compare the arrays.
        """
        if len(self) != len(other):
            return False
        if self.is_equidistant and other.is_equidistant:
            return self.xstart == other.xstart and self.xdelta == other.xdelta
        if self.is_equidistant != other.is_equidistant:
            return False
        return bool(np.array_equal(self.x, other.x))

    def __len__(self) -> int:
        return self._values.size

    @property
    def x(self) -> np.ndarray:
        return self._values.x()

    @property
    def y(self) -> np.ndarray:
        return self._values.y()

    def to_series(self):
        """This signal as a pandas Series indexed by x. Requires pandas."""
        from ._frames import signal_to_series  # pylint: disable=import-outside-toplevel

        return signal_to_series(self)

    def to(self, unit: str | None = None, xunit: str | None = None) -> Signal:
        """This signal in other units; this one is left unchanged.

        Values arrive in SIMA's base units, and this gives them in another --
        kN rather than N, mm rather than m, rad rather than deg. Nothing is
        copied: values are converted when read.

        :param unit: target for the values, or None to leave them.
        :param xunit: target for the x-axis, or None to leave it.
        :raises ValueError: if a target measures something else, or either label
            has no known conversion -- ``N`` converts to ``kN`` but not to ``m``.
        """
        if unit is None and xunit is None:
            return self
        y_factor = conversion_factor(self.unit, unit) if unit else 1.0
        x_factor = conversion_factor(self.xunit, xunit) if xunit else 1.0
        attributes = dict(self.attributes)
        attributes["unit"] = unit or self.unit
        attributes["xunit"] = xunit or self.xunit
        if "value" in attributes and y_factor != 1.0:
            attributes["value"] = _rescaled_text(attributes["value"], y_factor)
        converted = Signal(
            self.name,
            _Rescaled(self._values, x_factor, y_factor),
            **{key: value for key, value in attributes.items() if value is not None},
        )
        converted._parent = self._parent  # pylint: disable=protected-access
        return converted

    def __repr__(self) -> str:
        axis = (
            f" dx={self.xdelta:g}" if self.is_equidistant else ""
        )
        return (
            f"<Signal {self.name!r} n={len(self)} "
            f"unit={self.unit!r} xunit={self.xunit!r}{axis}>"
        )


class _Rescaled:
    """Values seen in a different unit, as :meth:`Signal.to` returns them.

    ``xstart`` and ``xdelta`` are rescaled rather than forwarded, because
    ``Signal.same_axis`` compares them and must agree with ``x()``.
    """

    # pylint: disable=missing-function-docstring  # implements the Values protocol

    def __init__(self, values, x_factor: float, y_factor: float):
        self._values = values
        self._x_factor = x_factor
        self._y_factor = y_factor
        for name in ("xstart", "xdelta"):
            axis = getattr(values, name, None)
            if axis is not None:
                setattr(self, name, axis * x_factor)

    @property
    def size(self) -> int:
        return self._values.size

    def x(self) -> np.ndarray:
        return _scaled(self._values.x(), self._x_factor)

    def y(self) -> np.ndarray:
        return _scaled(self._values.y(), self._y_factor)

    def __getattr__(self, name: str) -> Any:
        # Runs only for what this object does not hold, so reaching here for
        # xstart or xdelta means the wrapped values had none -- and the
        # AttributeError is what Signal.xstart reads as "not equidistant".
        if name == "_values":
            raise AttributeError(name)
        return getattr(self._values, name)


def _scaled(values: np.ndarray, factor: float) -> np.ndarray:
    if factor != 1.0:
        return values * factor
    view = values.view()
    view.flags.writeable = False
    return view


def _rescaled_text(value: str, factor: float) -> str:
    try:
        return str(float(value) * factor)
    except ValueError:
        return value


class ConstantValues:
    """A single value, the way a container holds one."""

    # pylint: disable=missing-function-docstring  # implements the Values protocol

    def __init__(self, value: object):
        self.value = value

    @property
    def size(self) -> int:
        return 1

    def x(self) -> np.ndarray:
        return np.zeros(1)

    def y(self) -> np.ndarray:
        return np.asarray([self.value])


def constant(name: str, value: object, **attributes: str) -> Signal:
    """A one-sample signal holding ``value``."""
    signal = Signal(name, ConstantValues(value), **attributes)
    signal._attributes["value"] = str(value)  # pylint: disable=protected-access
    return signal


class _NoValues:
    """Placeholder for a signal that failed to load."""

    # pylint: disable=missing-function-docstring  # implements the Values protocol

    def __init__(self, error: SourceError):
        self._error = error

    @property
    def size(self) -> int:
        return 0

    def x(self) -> np.ndarray:
        raise self._fresh()

    def y(self) -> np.ndarray:
        raise self._fresh()

    def _fresh(self) -> SourceError:
        # Re-raising one instance would grow its traceback on every access.
        error = type(self._error)(*self._error.args)
        error.__cause__ = self._error.__cause__
        return error


class ErrorSignal(Signal):
    """A read failure, placed in the tree where the data should have been.

    A failing reader does not abort the import, it leaves a marker behind.
    """

    def __init__(self, name: str, error: SourceError):
        super().__init__(name, _NoValues(error))
        self._error = error

    @property
    def error(self) -> SourceError:
        return self._error

    def __repr__(self) -> str:
        return f"<ErrorSignal {self.name!r}: {self.error}>"
