"""pandas views over the signal tree. Optional: ``pip install simapy[pandas]``.

**RIFLEX x-axes repeat values, and that is not a defect.** A curvature curve is
sampled at both ends of every element, so its x reads ``[0, 2, 2, 4, 4, ...]``.
pandas tolerates a duplicated index, but aligning two different x-axes on one
would silently invent data, so signals whose x-axes differ are refused rather
than joined. ``index=False`` gives positional semantics instead.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from ._node import DUPLICATE, Container, Signal

if TYPE_CHECKING:
    import pandas as pd

_MISSING = (
    "pandas is required for DataFrame support but is not installed. "
    "Install it with `pip install simapy[pandas]`, or use Signal.x / Signal.y, "
    "which are plain numpy arrays."
)


def _pandas():
    try:
        import pandas  # pylint: disable=import-outside-toplevel
    except ImportError as exc:
        raise ImportError(_MISSING) from exc
    return pandas


def signal_to_series(signal: Signal) -> pd.Series:
    """One signal as a Series indexed by its x-axis.

    Units and the signal's attributes go on ``.attrs``, which pandas drops
    through most operations.
    """
    pandas = _pandas()
    series = pandas.Series(
        signal.y,
        index=pandas.Index(signal.x, name=axis_name(signal)),
        name=signal.name,
    )
    series.attrs = {"unit": signal.unit, "xunit": signal.xunit, **signal.attributes}
    return series


def container_to_frame(
    container: Container, recursive: bool = False, index: bool = True
) -> pd.DataFrame:
    """A container's signals as a DataFrame sharing one x-axis.

    :param recursive: every signal below the container, not just its own. Works
        only when the whole subtree shares one x-axis.
    :param index: put x on the index. False puts it in a column named after its
        unit and leaves a RangeIndex -- better when x repeats.
    :raises ValueError: if there are no signals, or their x-axes differ.
    """
    if recursive:
        signals = [node for node in container.walk() if isinstance(node, Signal)]
    else:
        signals = list(container.signals)
    if not signals:
        raise ValueError(f"{container.name!r} has no signals to put in a frame")
    return signals_to_frame(signals, index=index)


def signals_to_frame(
    signals: Sequence[Signal], names: Sequence[str] | None = None, index: bool = True
) -> pd.DataFrame:
    """Any set of signals sharing one x-axis, as a DataFrame.

    :param names: column names, one per signal. By default the signal names,
        with SIMA's ``_duplicate_N`` on repeats; ``attrs["units"]`` follows
        whichever is used.
    :raises ValueError: if the signals do not all share an x-axis, or ``names``
        does not match them one to one.
    """
    pandas = _pandas()
    if not signals:
        raise ValueError("No signals given")
    _require_one_axis(signals)

    columns_names = list(names) if names is not None else _unique_names(signals)
    if len(columns_names) != len(signals) or len(set(columns_names)) != len(columns_names):
        raise ValueError("names must give each signal its own column name")

    first = signals[0]
    columns = {name: signal.y for name, signal in zip(columns_names, signals)}
    if index:
        frame = pandas.DataFrame(columns, index=pandas.Index(first.x, name=axis_name(first)))
    else:
        frame = pandas.DataFrame({axis_name(first): first.x, **columns})

    frame.attrs = {
        "units": {name: signal.unit for name, signal in zip(columns_names, signals)},
        "xunit": first.xunit,
    }
    return frame


def axis_name(signal: Signal) -> str:
    """What to call the x-axis: ``time`` for seconds, else the unit."""
    unit = signal.xunit
    return "time" if unit == "s" else (unit or "x")


def _require_one_axis(signals: Sequence[Signal]) -> None:
    first = signals[0]
    for signal in signals[1:]:
        if first.same_axis(signal):
            continue
        if len(first) != len(signal):
            why = f"{len(first)} vs {len(signal)} samples"
        else:
            why = f"same {len(first)} samples, different x values"
        raise ValueError(
            f"{first.name!r} and {signal.name!r} do not share an x-axis ({why}). "
            "Frame each container separately."
        )


def _unique_names(signals: Sequence[Signal]) -> list[str]:
    seen: dict[str, int] = {}
    names: list[str] = []
    for signal in signals:
        count = seen.get(signal.name, 0)
        seen[signal.name] = count + 1
        names.append(f"{signal.name}{DUPLICATE}{count}" if count else signal.name)
    return names
