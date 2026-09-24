"""Run Workflow with SIMA Runtime Engine.

This example demonstrates how run a SIMA workflow programmatically

The script shows the complete workflow of:
    1. Importing a workflow definition file
    2. Setting up the storage root to point to the current directory where the script is located
    3. Setting up input parameters (a scale value in this case)
    4. Running the workflow
    5. Processing and validating the results from the workflow execution


Example:
    Basic usage of this script:
    
    >>> python run_workflow_with_sre.py
    
"""
import os
import shutil
from pathlib import Path
from simapy.sre import SIMA
from simapy.results import open_results

def main():
    """Execute the main workflow example.
    
    Creates and runs a simple workflow using the SIMA Runtime Engine (SRE).
    The workflow takes a scale parameter and multiplies it by values from a signal.
    Results are validated after execution completes.
    """
    examples = Path(__file__).parents[1]
    ws = examples / "output" / "workflow" / "ws"
    if ws.exists():
        shutil.rmtree(ws, ignore_errors=True)
    os.makedirs(ws, exist_ok=True)

    json_file = examples / "input" / "workflow" / "workflow_task.json"
    # This will be used as an input
    scale = 3.0

    here = Path(__file__).parent
    # run_workflow cannot set a storage root, so the commands are spelled out.
    commands = [
        "--import", f"file={json_file.absolute()}",
        "--storageroot", "task=ExternalStorage", f"root={here}",
        "--run", "task=WorkflowTask", "workflow=workflow", f"input=scale={scale}",
    ]

    # Requires that the environment is set, but an alternative path may be given
    exe = os.getenv('SRE_EXE')
    # Set show_output to False to disable console output, this will make the progress bare more visible
    # The console output is still piped to a file within the workspace
    sima = SIMA(exe=exe,show_output=False)

    # Run the workflow with SRE
    sima.run(ws, commands)

    res = open_results(ws / "out.json")
    print(f"Successfully executed workflow! {len(res.select())} signals in out.json")

    sine = res.run.signal("some_data/mysine_frompy")
    print(f"   {sine.name}: {len(sine)} samples at dt={sine.xdelta:g} {sine.xunit}")

    mynum = res.run.signal("some_data/mynum_frompy")
    print(f"   {mynum.name}={mynum.y[0]}")
    if mynum.y[0] != scale:
        raise ValueError(f"Number not as expected {mynum.y[0]} vs {scale}")


if __name__ == "__main__":
    main()
