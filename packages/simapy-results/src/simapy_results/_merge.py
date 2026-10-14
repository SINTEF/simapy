"""Merging two subtrees, as SIMA's ``SignalItemUtil.mergeContainers`` does.

* Same-named containers merge unless both set one attribute to different
  values; attributes are unioned. Such a pair stays separate and warns.
* Signals are appended without deduplication.
* Siblings are sorted with SIMA's comparator, quirks included.
"""

from __future__ import annotations

from functools import cmp_to_key

from ._build import add_signal, merge_attributes, replace_containers
from ._node import INDEX, Container
from ._sources import warn


def merge_containers(c1: Container, c2: Container) -> None:
    """Merge ``c2`` into ``c1``. ``c2`` is consumed."""
    merge_attributes(c1, c2)
    items: list[Container] = [*c1.containers, *c2.containers]
    replace_containers(c1, merge_items(items))
    for signal in c2.signals:
        add_signal(c1, signal)


def merge_items(items: list[Container]) -> list[Container]:
    """Pair containers by name, merge the mergeable ones, then sort."""
    if len(items) == 1:
        return list(items)

    result: list[Container] = []
    consumed: set[int] = set()
    for i, first in enumerate(items):
        if i in consumed:
            continue
        result.append(first)
        for j in range(i + 1, len(items)):
            if j in consumed:
                continue
            second = items[j]
            if first.name == second.name and _can_merge(first, second):
                merge_containers(first, second)
                consumed.add(j)
    return _java_sort(result)


#: Java's ``TimSort.MIN_MERGE``: below it, ``List.sort`` is one run plus binary insertion.
_MIN_MERGE = 32


def _java_sort(items: list[Container]) -> list[Container]:
    """``List.sort`` with :func:`_compare`, step for step.

    The comparator is not a total order, so the result depends on the
    algorithm, and CPython's own sort changed in 3.13. Lists of 32 or more fall
    back to Python's sort, which agrees with Java whenever the order is total.
    """
    a = list(items)
    n = len(a)
    if n < 2:
        return a
    if n >= _MIN_MERGE:
        return sorted(a, key=cmp_to_key(_compare))
    # countRunAndMakeAscending
    run = 2
    if _compare(a[1], a[0]) < 0:
        while run < n and _compare(a[run], a[run - 1]) < 0:
            run += 1
        a[:run] = a[run - 1::-1]
    else:
        while run < n and _compare(a[run], a[run - 1]) >= 0:
            run += 1
    # binarySort
    for start in range(run, n):
        pivot = a[start]
        left, right = 0, start
        while left < right:
            mid = (left + right) >> 1
            if _compare(pivot, a[mid]) < 0:
                right = mid
            else:
                left = mid + 1
        a[left + 1:start + 1] = a[left:start]
        a[left] = pivot
    return a


def _can_merge(c1: Container, c2: Container) -> bool:
    shared = c1.attributes.keys() & c2.attributes.keys()
    conflicts = {key for key in shared if c1.attributes[key] != c2.attributes[key]}
    if conflicts:
        warn(
            f"not merging two containers named {c1.name!r}: they disagree on "
            f"{', '.join(sorted(conflicts))}. Merging would discard one side."
        )
        return False
    return True


def _compare(c1: Container, c2: Container) -> int:
    """SIMA's sibling comparator, ported verbatim.

    Not a total order: an untyped node ties with everything, and same-typed
    nodes tie unless both have an index.
    """
    t1, t2 = c1.type, c2.type
    if t1 == t2:
        i1, i2 = _index_of(c1), _index_of(c2)
        if i1 is not None and i2 is not None:
            return (i1 > i2) - (i1 < i2)
        return 0
    if t1 is not None and t2 is not None:
        return (t1 > t2) - (t1 < t2)
    return 0


def _index_of(item: Container) -> int | None:
    raw = item.attributes.get(INDEX)
    if raw is None:
        return None
    try:
        return int(raw)
    except ValueError:
        return None
