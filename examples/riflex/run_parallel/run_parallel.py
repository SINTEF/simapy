"""Run Parallel Conditions.

This example demonstrates running multiple SIMA conditions in parallel with different input parameters.
It also shows how to post-process results from multiple runs, first in each run and then in the main thread after all runs are completed.

The example uses a Riflex task to analyze a simple beam with different wave conditions.

After each run, the maximum axial force is calculated and stored in the result file.
After all runs are completed, a summary file is created with the maximum axial force for each run and the overall maximum.


Environment variable `SRE_EXE` is used to point to the sre executable of SIMA if exe is not provided directly in create_run.

"""

import os
import shutil
from pathlib import Path
import h5py
import numpy as np
from utils.runner import run_multiple


def __create_run(
    output_folder: Path, stask: Path, variables: dict, cleanup: bool = False
):
    """Create a run configuration for a single run with SIMA.

    Args:
        output_folder (Path): Base directory where all outputs will be stored
        stask (Path): Path to the SIMA task file (.stask) to be executed
        variables (dict): Dictionary of input variables and their values (e.g., {"Hs": 2.0, "Tp": 5.0})
        cleanup (bool, optional): Whether to clean up temporary files after execution. Defaults to False.

    Returns:
        dict: Run configuration dictionary with name, workspace, commands, and settings
    """
    case_name = "_".join([f"{key}={value}" for key, value in variables.items()])
    ws = output_folder / "tmp" / case_name
    result_folder = output_folder / "results" / case_name
    if result_folder.exists():
        shutil.rmtree(result_folder, ignore_errors=True)

    task = "SimpleBeam"
    condition = "Initial"
    # Create input string from variables
    input = ";".join([f"{key}={value}" for key, value in variables.items()])
    runType = "dynamic"
    # Export all the results into the result file
    result_file = result_folder / "result.h5"

    commands = []
    # Import the Riflex task from an stask file
    commands.append("--import")
    commands.append(f"file={stask.absolute()}")
    # Run dynamic analysis for the specified condition
    commands.append("--condition")
    commands.append(f"task={task}")
    commands.append(f"condition={condition}")
    commands.append(f"runType={runType}")
    # Export all the results into the result file
    commands.append(f"output={result_file}")
    commands.append(f"input={input}")
    # Copy the result files to the result folder
    commands.append("copy=true")
    commands.append("paths=*.res;*.inp")
    commands.append(f"destination={result_folder}")

    # Postprocess function that will be called after the run is completed
    def post():
        __process_single(result_folder, task, condition)
        # Copy the log file to the result folder
        shutil.copy(ws / "sima.log", result_folder)
        if cleanup:
            # Remove workspace folder
            shutil.rmtree(ws, ignore_errors=True)

    # Provide the path to SRE executable if not set in environment SRE_EXE
    exe = None
    return {
        "name": case_name,
        "exe": exe,
        "ws": ws,
        "commands": commands,
        "postprocess": post,
        "result_file": result_file,
        "task": task,
        "condition": condition,
        "cleanup": cleanup,
    }


def __process_single(result_folder: Path, task: str, condition: str):
    """Post-process results from a single SIMA run.

    Calculates the maximum axial force for the given element and stores it back into the result file.

    Args:
        result_folder (Path): Directory containing the result files from the analysis
        task (str): Name of the task
        condition (str): Name of the condition
    """
    file = result_folder / "result.h5"
    # We want to both read and write to the file
    with h5py.File(file, "r+") as f:
        # Get the element from the file
        element = f[f"/{task}/{condition}/Dynamic/BeamLine/segment_1/element_1"]
        # Get the axial force from the element
        axial_force = element["Axial force"][:]
        # Calculate the maximum axial force
        max_force = np.max(axial_force)
        # Store the maximum axial force back into the file
        element.create_dataset("axial_force_max", data=[max_force])


def __process_multiple(runs: list[dict], output_folder: Path):
    """Perform combined analysis of results from multiple parallel runs.

    Creates a summary file with maximum axial forces from each run and identifies
    the overall maximum across all conditions.
    """
    # Pick up all the result files to do some combined analysis
    # Write a summary file
    summary_file = output_folder / "summary.txt"
    with open(summary_file, "w") as summary:
        max_forces = []
        for run in runs:
            result_file = run["result_file"]
            task = run["task"]
            condition = run["condition"]
            element_path = f"/{task}/{condition}/Dynamic/BeamLine/segment_1/element_1"
            with h5py.File(result_file, "r") as f:
                element = f[element_path]
                axial_force_max = element["axial_force_max"][:]
                summary.write(f"{run['name']}: {axial_force_max}\n")
                max_forces.append(axial_force_max)
        summary.write(f"Max force: {np.max(max_forces)}\n")


if __name__ == "__main__":
    here = Path(__file__).parent.absolute()
    examples_root = (here / "../../../").resolve()
    output_folder = examples_root / "output" / "run_parallel"
    input_folder = examples_root / "input"

    # Flag for cleanup, will remove working folders if True
    cleanup = True

    if cleanup:
        shutil.rmtree(output_folder, ignore_errors=True)
    os.makedirs(output_folder, exist_ok=True)

    stask = input_folder / "riflex" / "simple_beam.stask"

    # Prepare runs before sending them to the executor
    runs = []
    runs.append(__create_run(output_folder, stask, {"Hs": 2.0, "Tp": 5.0}, cleanup=cleanup))
    runs.append(__create_run(output_folder, stask, {"Hs": 3.0, "Tp": 6.0}, cleanup=cleanup))
    runs.append(__create_run(output_folder, stask, {"Hs": 4.0, "Tp": 7.0}, cleanup=cleanup))

    # Schedule runs
    run_multiple(runs)

    # Then postprocess after all are done
    __process_multiple(runs, output_folder)

    tmp_folder = output_folder / "tmp"
    if cleanup:
        # Remove tmp folder
        shutil.rmtree(tmp_folder, ignore_errors=True)
