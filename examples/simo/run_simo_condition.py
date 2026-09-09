"""Run a SIMO condition from a task file.

Demonstrates importing a SIMA task file (stask) and running a specific 
condition using the SIMA Runtime Engine (SRE).

Requirements:
    - Environment variable `SRE_EXE` which points to the SIMA executable
    - Input file: 'input/simo/simo.stask'

Example:
    >>> python run_simo_condition.py
"""
import os
import shutil
from pathlib import Path

from simapy.sre import SIMA


def main():
    """Run a SIMO simulation condition using SRE.
    
    Imports a predefined SIMA task file and runs a specific condition.
    Clears the workspace before running for a clean execution environment.
    """
    ws = Path("output/simo/condition")
    if ws.exists():
        shutil.rmtree(ws, ignore_errors=True)
    os.makedirs(ws, exist_ok=True)

    stask = Path("input/simo/simo.stask")

    commands = []
    commands.append("--import")
    commands.append("file=" + str(stask.absolute()))
    commands.append("--condition")
    commands.append("task=BouncingBalls")
    commands.append("condition=conditionSet")
    commands.append("runType=dynamic")

    # Requires that the environment is set, but an alternative path may be given
    exe = os.getenv("SRE_EXE")
    sima = SIMA(exe=exe)
    sima.run(ws, commands)
    
    print(f"SIMO condition executed successfully. Results in {ws}")


if __name__ == "__main__":
    main()
