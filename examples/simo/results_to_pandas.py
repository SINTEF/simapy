"""Results as pandas objects: a Series, a DataFrame, and one column per member.

`simapy.results` hands out numpy arrays, and every signal and container also
converts to pandas. This shows the three shapes, and the one rule that is not
obvious: a frame has one x-axis, so it is one container.

It reads what `run_simo_condition.py` produced -- three runs of a bouncing-ball
model with different contact stiffness `kzz` -- and runs the condition first if
those results are not there yet.

Requirements:
    - Environment variable `SRE_EXE`, if the condition still has to be run
    - pandas and matplotlib

Example:
    Basic usage of this script:

    >>> python simo/results_to_pandas.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # write PNGs without a display, so this works over SSH and in CI

import matplotlib.pyplot as plt  # noqa: E402  the backend must be chosen first
import pandas as pd  # noqa: E402

try:
    # Run as a script: this file's own directory is on sys.path.
    from read_simo_results import EXAMPLES, HEIGHT, PLOTS, condition_members, kzz
except ModuleNotFoundError:
    # Imported as examples.simo.results_to_pandas, which is how the docs
    # autodoc this module.
    from examples.simo.read_simo_results import EXAMPLES, HEIGHT, PLOTS, condition_members, kzz

from simapy.results import signals_to_frame  # noqa: E402

#: The container framed below. Its six signals share one time axis.
POSITION = "Dynamic/BALL2/Global total position"


def a_series(member) -> pd.Series:
    """One signal as a Series indexed by its x-axis.

    The units travel with it in `attrs`, which is what keeps a plot or a report
    from having to be told what it is looking at a second time.

    Args:
        member: One member's container.

    Returns:
        The ball's height, indexed by time.
    """
    series = member.signal(HEIGHT).to_series()

    print(f"-- {series.name} as a Series " + "-" * 40)
    print(f"   index {series.index.name!r}, {series.attrs}")
    print(f"   first 0.1 s:  {', '.join(f'{v:.3f}' for v in series.loc[0.0:0.1])}")
    # Anything pandas does to a Series, it does to this one.
    print(f"   settles at:   {series.tail(len(series) // 10).mean():.3f} "
          f"(mean of the last tenth)")
    return series


def a_frame(member) -> pd.DataFrame:
    """One container as a DataFrame, one column per signal.

    Args:
        member: One member's container.

    Returns:
        BALL2's six position signals on a shared time index.
    """
    frame = member.container(POSITION).to_dataframe()

    print(f"\n-- {POSITION} as a DataFrame " + "-" * 20)
    print(f"   {len(frame.columns)} columns on a {frame.index.name!r} index")
    # A DataFrame has nowhere to put a unit per column, so the frame carries
    # them beside it. The columns here are not all in metres.
    print(f"   units: {frame.attrs['units']}")
    print(frame.describe().T.to_string(float_format=lambda v: f"{v:10.3f}"))
    return frame


def why_one_container(member) -> None:
    """Show what framing a whole member refuses to do, and why.

    Aligning signals that do not share an x-axis would have to invent values,
    so it raises instead of guessing. Here the member's `kzz` variable is one
    sample and its time series are thousands.

    Args:
        member: One member's container.
    """
    print("\n-- a frame is one x-axis " + "-" * 32)
    try:
        member.to_dataframe(recursive=True)
    except ValueError as refusal:
        print(f"   {refusal}")


def one_column_per_member(members) -> pd.DataFrame:
    """The same signal from every member, side by side.

    The three runs are the same model at different stiffness, so they do share
    an axis and can go in one frame. By default the columns would all be called
    after the signal; `names` says what to call them instead.

    Args:
        members: One container per member.

    Returns:
        BALL2's height per member, columns named by `kzz`.
    """
    heights = [member.signal(HEIGHT) for member in members]
    frame = signals_to_frame(heights, names=[f"kzz={kzz(m):,.0f}" for m in members])

    print("\n-- the same signal from every member " + "-" * 20)
    print(frame.describe().T.to_string(float_format=lambda v: f"{v:10.3f}"))
    print("\n   correlation between members")
    print(frame.corr().to_string(float_format=lambda v: f"{v:8.3f}"))
    return frame


def plot_frame(frame: pd.DataFrame, quantity: str, title: str, folder: Path) -> Path:
    """Plot straight off the frame, taking the units from what it carries.

    Args:
        frame: A frame whose columns all measure one quantity, as
            `one_column_per_member` returns.
        quantity: What the columns measure, for the y-axis label.
        title: The figure title.
        folder: Where the PNG goes.

    Returns:
        The file written.
    """
    axes = frame.plot(figsize=(8, 4), linewidth=0.9)
    axes.set_xlabel(f"Time [{frame.attrs['xunit']}]")
    axes.set_ylabel(f"{quantity} [{frame.attrs['units'][frame.columns[0]]}]")
    axes.set_title(title)

    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "ball2_height_frame.png"
    axes.figure.savefig(path, dpi=120, bbox_inches="tight")
    plt.close(axes.figure)
    return path


def main():
    """Convert one condition set to pandas, three ways."""
    # Sorted so the columns below read softest spring first, rather than in
    # the order SIMA lists the members in.
    members = sorted(condition_members(), key=kzz)

    a_series(members[0])
    a_frame(members[0])
    why_one_container(members[0])
    frame = one_column_per_member(members)

    quantity = members[0].signal(HEIGHT).name
    path = plot_frame(frame, quantity, "BALL2 height, by contact stiffness", PLOTS)
    print(f"\n   wrote {path.relative_to(EXAMPLES)}\n")


if __name__ == "__main__":
    main()
