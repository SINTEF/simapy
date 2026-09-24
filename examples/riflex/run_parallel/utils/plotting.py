"""Plot helpers for the parallel run analysis.

These take `Signal` objects rather than arrays, so every axis label is
``name [unit]`` from the signal itself. PNGs are written with a non-interactive
backend, so it works headless and in CI.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Sequence

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402  the backend must be set first

from simapy.results import Signal  # noqa: E402

plt.rcParams.update({
    "figure.dpi": 120,
    "savefig.dpi": 120,
    "savefig.bbox": "tight",
    "font.size": 9,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "legend.frameon": False,
})


def label(signal: Signal, name: str | None = None) -> str:
    """``name [unit]``, the unit taken from the signal.

    ``name`` defaults to the signal's own; an empty one leaves just the unit.
    Empty units are dropped.
    """
    return _with_unit(signal.name if name is None else name, signal.unit)


def x_label(signal: Signal, name: str | None = None) -> str:
    """The x-axis equivalent: seconds are Time, metres Line length, else just the unit."""
    if name is None:
        name = {"s": "Time", "m": "Line length"}.get(signal.xunit, "")
    return _with_unit(name, signal.xunit)


def _with_unit(text: str, unit: str | None) -> str:
    if not unit or unit == "-":
        return text
    return f"{text} [{unit}]" if text else f"[{unit}]"


def save(fig, folder: Path, name: str) -> Path:
    """Write to ``<folder>/<name>.png`` and return the path."""
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{name}.png"
    fig.savefig(path)
    plt.close(fig)
    return path


def curves(
    signals: Sequence[Signal],
    folder: Path,
    title: str,
    name: str,
    labels: Sequence[str] | None = None,
    x_name: str | None = None,
    y_name: str | None = None,
) -> Path:
    """Several signals sharing an axis, on one set of axes."""
    fig, ax = plt.subplots(figsize=(7.5, 4))
    for index, signal in enumerate(signals):
        text = labels[index] if labels else signal.name
        ax.plot(signal.x, signal.y, linewidth=1.2, label=text)
    first = signals[0]
    ax.set_xlabel(x_label(first, x_name))
    ax.set_ylabel(label(first, y_name or _shared_name(signals)))
    ax.set_title(title)
    if len(signals) > 1 or labels:
        ax.legend()
    return save(fig, folder, name)


def bars(
    names: Sequence[str],
    values: Sequence[float],
    folder: Path,
    title: str,
    name: str,
    value_unit: str,
    value_name: str = "value",
) -> Path:
    """One number per case, when the comparison matters more than the curve."""
    fig, ax = plt.subplots(figsize=(7.5, 0.5 * len(names) + 2))
    positions = range(len(names))
    ax.barh(list(positions), list(values), height=0.6)
    ax.set_yticks(list(positions), list(names))
    ax.set_xlabel(f"{value_name} [{value_unit}]" if value_unit else value_name)
    ax.set_title(title)
    ax.invert_yaxis()
    span = max(values) - min(values)
    for position, value in zip(positions, values):
        ax.text(value + span * 0.02 if span else value, position,
                f"{value:,.0f}", va="center", fontsize=8)
    ax.set_xlim(right=max(values) + (span if span else max(values) * 0.1) * 0.25)
    return save(fig, folder, name)


def _shared_name(signals: Iterable[Signal]) -> str:
    """A y-axis name for several signals: the common one, or just the unit."""
    names = {s.name for s in signals}
    return names.pop() if len(names) == 1 else ""
