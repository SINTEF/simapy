"""Run Parallel Conditions.

This example demonstrates running multiple SIMA conditions in parallel with different input parameters.
It also shows how to post-process results from multiple runs, first in each run and then in the main thread after all runs are completed.

The example uses a Riflex task to analyze a simple beam with different wave conditions.

After each run, its maximum axial force is reported.
After all runs are completed, a summary file is created with the maximum axial force for each run and the overall maximum.

Environment variable `SRE_EXE` is used to point to the sre executable of SIMA if exe is not provided directly in _create_run.
"""

import os
import shutil
from pathlib import Path
from utils import plotting
from utils.runner import run_multiple
from simapy.results import open_results, ResultSet


#: The element both post-processing steps look at.
ELEMENT = "Dynamic/BeamLine/segment_1/element_1"


def _create_run(output_folder: Path, stask: Path, variables: dict):
    """Create a run configuration for a single run with SIMA.

    Args:
        output_folder (Path): Base directory where all outputs will be stored
        stask (Path): Path to the SIMA task file (.stask) to be executed
        variables (dict): Dictionary of input variables and their values (e.g., {"Hs": 2.0, "Tp": 5.0})

    Returns:
        dict: Run configuration: name, workspace, condition, variables and post-processing
    """
    case_name = "_".join([f"{key}={value}" for key, value in variables.items()])
    ws = output_folder / "tmp" / case_name
    result_folder = output_folder / "results" / case_name
    if result_folder.exists():
        shutil.rmtree(result_folder, ignore_errors=True)

    def post(res):
        """Report on this case as soon as it finishes."""
        _process_single(res, case_name)
        shutil.copy(ws / "sima.log", result_folder)

    return {
        "name": case_name,
        # Provide the path to SRE executable if not set in environment SRE_EXE
        "exe": None,
        "ws": ws,
        "stask": stask,
        "task": "SimpleBeam",
        "condition": "Initial",
        "run_type": "dynamic",
        "variables": variables,
        # Copying the results out lets the workspace be discarded afterwards.
        "results_dir": result_folder,
        "postprocess": post,
    }


def _process_single(res: ResultSet, case_name: str):
    """Report the peak axial force from a single run, as soon as it finishes.

    Args:
        res: The `ResultSet` for this run
        case_name (str): The case this run is, used only if it carries no variables
    """
    signal = res.run.signal(f"{ELEMENT}/Axial force")
    print(f"   {_sea_state(res) or case_name:18} peak axial force "
          f"{signal.y.max():>14,.0f} {signal.unit}")


def _process_multiple(runs: list[dict], output_folder: Path):
    """Compare the runs, and report and plot what the sweep did."""
    # Read each result folder back, this time with all three runs in hand.
    cases = [open_results(run["results_dir"]) for run in runs]

    # What each run is and which files it was read from.
    print()
    print(f"-- {len(cases)} runs, one folder each " + "-" * 40)
    for case in cases:
        read = [s for s in case.sources if s.signals]
        files = ", ".join(f"{s.file} ({s.signals})" for s in read)
        print(f"   {case.description.condition:20} {_sea_state(case):18} {files}")

    # The same signal from every run, side by side.
    axial = [case.run.signal(f"{ELEMENT}/Axial force") for case in cases]
    print("\n-- axial force in element_1 " + "-" * 44)
    print(f"   {'sea state':18}{'min':>16}{'max':>16}{'mean':>16}{'std':>14}")
    for case, signal in zip(cases, axial):
        y = signal.y
        print(f"   {_sea_state(case):18}{y.min():>16,.0f}{y.max():>16,.0f}"
              f"{y.mean():>16,.0f}{y.std():>14,.0f}")
    print(f"   values in {axial[0].unit}, {len(axial[0])} samples at "
          f"dt={axial[0].xdelta:g} {axial[0].xunit}")

    # One figure for the curves, one for the peaks alone.
    labels = [_sea_state(case) for case in cases]
    plots = output_folder / "plots"
    written = [
        plotting.curves(axial, plots, "Axial force in element_1, one curve per sea state",
                        "axial_force", labels=labels, y_name="Axial force"),
        plotting.bars(labels, [s.y.max() for s in axial], plots,
                      "Peak axial force per sea state", "axial_force_peaks",
                      axial[0].unit, "Peak axial force"),
    ]

    # The peak per run and the overall peak, for whatever reads this next.
    summary_file = output_folder / "summary.txt"
    with open(summary_file, "w", encoding="utf-8") as summary:
        for case, signal in zip(cases, axial):
            summary.write(f"{case.description.condition}: {signal.y.max()}\n")
        summary.write(f"Max force: {max(s.y.max() for s in axial)}\n")

    print()
    for path in [summary_file, *written]:
        print(f"   wrote {path.relative_to(output_folder)}")


def _sea_state(case) -> str:
    """A case label from the values that run used, not from its folder name."""
    v = case.description.variables
    return ", ".join(f"{n}={v[n].value:g}" for n in ("Hs", "Tp") if n in v)


if __name__ == "__main__":
    here = Path(__file__).parent.absolute()
    examples_root = (here / "../..").resolve()
    output_folder = examples_root / "output" / "run_parallel"
    input_folder = examples_root / "input"

    # Flag for cleanup, will remove working folders if True
    cleanup = True

    if cleanup:
        shutil.rmtree(output_folder, ignore_errors=True)
    os.makedirs(output_folder, exist_ok=True)

    stask = input_folder / "riflex" / "simple_beam.stask"

    # Prepare runs before sending them to the executor
    runs = [
        _create_run(output_folder, stask, {"Hs": 2.0, "Tp": 5.0}),
        _create_run(output_folder, stask, {"Hs": 3.0, "Tp": 6.0}),
        _create_run(output_folder, stask, {"Hs": 4.0, "Tp": 7.0}),
    ]

    completed = run_multiple(runs)

    # Then postprocess after all are done
    if completed:
        _process_multiple(completed, output_folder)

    if cleanup:
        shutil.rmtree(output_folder / "tmp", ignore_errors=True)

    if len(completed) < len(runs):
        raise SystemExit(f"{len(runs) - len(completed)} of {len(runs)} runs failed")
