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
from simapy.sima_reader import SIMAReader
from simapy.sima import signals

def main():
    """Execute the main workflow example.
    
    Creates and runs a simple workflow using the SIMA Runtime Engine (SRE).
    The workflow takes a scale parameter and multiplies it by values from a signal.
    Results are validated after execution completes.
    """
    output = Path("output/workflow")
    ws = output / "ws"
    if ws.exists():
        shutil.rmtree(ws, ignore_errors=True)
    os.makedirs(ws, exist_ok=True)

    input = Path(__file__).parent / ".." / ".." / "input"
    json_file = input / "workflow" / "workflow_task.json"
    # This will be used as an input
    scale = 3.0

    here =  Path(__file__).parent
    commands = []
    # First we import the json file to import the workflow
    commands.append("--import")
    commands.append("file=" + str(json_file.absolute()))
    # Then we set the storage root to the current directory
    commands.append("--storageroot")
    commands.append("task=ExternalStorage")
    commands.append("root=" + str(here))
    # Then we run the workflow
    commands.append("--run")
    commands.append("task=WorkflowTask")
    commands.append("workflow=workflow")
    commands.append(f"input=scale={scale}")

    # Requires that the environment is set, but an alternative path may be given
    exe = os.getenv('SRE_EXE')
    # Set show_output to False to disable console output, this will make the progress bare more visible
    # The console output is still piped to a file within the workspace
    sima = SIMA(exe=exe,show_output=False)
    
    # Run the workflow with SRE
    sima.run(ws, commands)
    
    # Read and validate the output
    output = ws / "out.json"
    sima_reader = SIMAReader()
    items = sima_reader.read(output)
    
    # Print validation results
    if len(items) == 1:
        print("Successfully executed workflow!")
        # Access the result signal
        container: signals.Container = items[0]
        mynum: signals.DimensionalScalar = container.signals[1]
        print(f"{mynum.name}={mynum.value}")
        if mynum.value != scale:
            raise ValueError(f"Number not as expected {mynum.value} vs {scale}")

    else:
        print("Failed to execute workflow or read results")


if __name__ == "__main__":
    main()
