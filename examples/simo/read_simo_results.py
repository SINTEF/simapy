"""Compare the members of a SIMO condition set, with a table and two plots.

`run_simo_condition.py` runs a bouncing-ball model three times, varying the
vertical stiffness `kzz` of a contact spring. This reads the condition set back,
tabulates what changed and plots it.

It shows the whole shape of a comparison: open the condition, take its members,
then summarise with pandas and plot with matplotlib.

Runs the condition first if its results are not there yet, so this works on a
clean checkout.

Requirements:
    - Environment variable `SRE_EXE`, if the condition still has to be run
    - pandas and matplotlib

Example:
    Basic usage of this script:

    >>> python simo/read_simo_results.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # write PNGs without a display, so this works over SSH and in CI

import matplotlib.pyplot as plt  # noqa: E402  the backend must be chosen first
import pandas as pd  # noqa: E402

try:
    # Run as a script: this file's own directory is on sys.path.
    from run_simo_condition import CONDITION, EXAMPLES, TASK, WORKSPACE, main as run_condition
except ModuleNotFoundError:
    # Imported as examples.simo.read_simo_results, which is how the docs
    # autodoc this module.
    from examples.simo.run_simo_condition import (CONDITION, EXAMPLES, TASK, WORKSPACE,
                                                  main as run_condition)
from simapy.results import ResultsError, open_results  # noqa: E402

#: What run_simo_condition.py left behind: <workspace>/<task>/<condition>.
RESULTS = WORKSPACE / TASK / CONDITION

#: Where the figures go.
PLOTS = WORKSPACE / "plots"

#: The signal this example plots, relative to a member.
HEIGHT = "Dynamic/BALL2/Global total position/ZG translation"


def kzz(member) -> float:
    """The contact stiffness this member ran with."""
    return float(member.signal("Variables/kzz").y[0])


def summarise(members) -> pd.DataFrame:
    """One row per member: the statistics of the ball's height.

    Args:
        members: One container per member, as `condition_members` returns.

    Returns:
        A DataFrame indexed by `kzz`.
    """
    rows = {}
    for member in members:
        series = member.signal(HEIGHT).to_series()
        rows[kzz(member)] = series.describe()[["min", "max", "mean", "std"]]
    frame = pd.DataFrame(rows).T
    frame.index.name = "kzz"
    return frame.sort_index()


def plot_height(members, folder: Path) -> Path:
    """Height against time, one curve per member."""
    fig, ax = plt.subplots(figsize=(8, 4))
    for member in sorted(members, key=kzz):
        signal = member.signal(HEIGHT)
        ax.plot(signal.x, signal.y, linewidth=0.9, label=f"kzz = {kzz(member):,.0f}")
    reference = members[0].signal(HEIGHT)
    ax.set_xlabel(f"Time [{reference.xunit}]")
    ax.set_ylabel(f"{reference.name} [{reference.unit}]")
    ax.set_title("BALL2 height, by contact stiffness")
    ax.legend()
    return _save(fig, folder, "ball2_height")


def plot_resting(members, folder: Path) -> Path:
    """Where the ball comes to rest, per member.

    Every run is dropped from the same height, so the maximum is identical in
    all three and says nothing. Where it settles is the part that responds.
    """
    ordered = sorted(members, key=kzz)
    labels = [f"{kzz(member):,.0f}" for member in ordered]
    signals = [member.signal(HEIGHT) for member in ordered]
    # The last tenth of the run, by which point the ball has stopped moving.
    resting = [float(s.y[-(len(s) // 10):].mean()) for s in signals]
    unit = signals[0].unit

    fig, ax = plt.subplots(figsize=(8, 3.2))
    bars = ax.barh(labels, resting, height=0.6)
    ax.bar_label(bars, fmt=f"%.1f {unit}", padding=4)
    ax.set_xlabel(f"Resting {signals[0].name} [{unit}]")
    ax.set_ylabel("Contact stiffness kzz")
    ax.set_title("Where BALL2 settles, by contact stiffness")
    ax.set_xlim(min(resting) * 1.25, 0)
    return _save(fig, folder, "ball2_resting")


def _save(fig, folder: Path, name: str) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{name}.png"
    fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    return path


def condition_members():
    """The set's members, running the condition first if it has not been.

    Returns:
        One container per member, as SIMA shows it below the set.
    """
    try:
        res = open_results(RESULTS)
    except ResultsError:
        # Produce them rather than refusing: depending on someone having run
        # run_simo_condition.py first makes this fail on a clean checkout.
        print(f"No results in {RESULTS.relative_to(EXAMPLES)} yet -- running the condition first.\n")
        res = run_condition()
    return [c for c in res.run.containers if c.type == "condition"]


def main():
    """Read the condition set and report on it."""
    members = condition_members()

    stiffness = ", ".join(f"{kzz(member):,.0f}" for member in sorted(members, key=kzz))
    print(f"\n{RESULTS.relative_to(EXAMPLES)}")
    print(f"   {len(members)} members, kzz = {stiffness}")

    height = members[0].signal(HEIGHT)
    print(f"\n-- BALL2 height, {len(height):,} samples at dt={height.xdelta:.2f} {height.xunit} --")
    print(summarise(members).to_string(float_format=lambda v: f"{v:10.3f}"))

    print()
    for path in (plot_height(members, PLOTS), plot_resting(members, PLOTS)):
        print(f"   wrote {path.relative_to(EXAMPLES)}")
    print()


if __name__ == "__main__":
    main()
