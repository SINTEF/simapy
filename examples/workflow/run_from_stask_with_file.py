"""Run Workflow from Task File with Input Signals.

This example demonstrates how to run a SIMA workflow defined in an external .stask file
using the SIMAPy API and the SIMA Runtime Engine (SRE).

The script shows the complete workflow of:
    1. Creating input signals and writing them to a file
    2. Importing a pre-defined workflow from a .stask file
    3. Executing the workflow with SRE
    4. Reading and processing the workflow results from output files

Features:
    Workflow File Integration:
        Shows how to use externally defined workflows (.stask files)
    Signal Generation:
        Creates input signals programmatically
    File I/O:
        Demonstrates reading and writing signal data from/to files
    Results Processing:
        Extracts and displays structured data from workflow output

Requirements:
    - Environment variable `SRE_EXE` must be set to point to the SIMA Runtime executable
    - A .stask file containing the workflow definition (included in repository)

Example:
    Basic usage of this script:
    
    >>> python run_from_stask_with_file.py
    
    This example can be adapted to work with any workflow defined in a .stask file
    by modifying the input signals and output processing as needed.
"""
import os
import shutil
from pathlib import Path
from simapy.sre import SIMA
from simapy.results import open_results
from simapy.sima_writer import SIMAWriter
from simapy.sima.signals.equallyspacedsignal import EquallySpacedSignal


def main():
    """Execute the workflow from .stask file example.
    
    Creates input signals, writes them to a file, imports a workflow from a .stask file,
    runs the workflow, and processes the results.
    """
    examples = Path(__file__).parents[1]
    ws = examples / "output" / "workflow" / "stask_with_file"
    if ws.exists():
        shutil.rmtree(ws, ignore_errors=True)
    os.makedirs(ws, exist_ok=True)

    # Create input signals
    a = EquallySpacedSignal(name="a")
    a.value = [1.0, 2.0, 3.0]
    b = EquallySpacedSignal(name="b")
    b.value = [3.0, 4.0, 5.0]

    # Write signals to input file
    SIMAWriter().write([a, b], ws / "input.json")

    # Locate stask file in the examples "input" folder
    stask = examples / "input" / "workflow" / "simple_workflow_run.stask"

    # Run the workflow with SRE
    exe = os.getenv('SRE_EXE')
    sima = SIMA(exe=exe)
    sima.run_workflow(ws, task="WorkflowTask", workflow="outer", stask=stask)

    # Process results
    output = ws / "Output/output.json"
    process_results(output)


def process_results(output_file: Path):
    """Process and display the results from the workflow execution.
    
    Args:
        output_file: Path to the output JSON file containing workflow results
    """
    res = open_results(output_file)
    found = res.select()
    if not found:
        print("No results found in output file")
        return

    # One path per run, nested exactly as the workflow nested its output.
    for path, signal in found.items():
        print(f"{path}={signal.y[0]}")


if __name__ == "__main__":
    main()
