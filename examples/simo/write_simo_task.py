"""Create a SIMO task from scratch and export as JSON.

This example demonstrates how to programmatically create a SIMO task and model
with a simple body and export it to a JSON file for later use in SIMA.

Example:
    Basic usage of this script:
    
    >>> python write_simo_task.py
    
    The script generates a SIMO task file in the output/simo/ directory.
"""
import os
from pathlib import Path
from simapy.sima import simo
from simapy.sima import hydro

from simapy.sima_writer import SIMAWriter


def main():
    task = simo.SIMOTask(name="test", model=simo.SIMOModel())
    body = simo.SIMOBody(name="body", _type=simo.BodyType.THREE_DOF_TIME_DOMAIN)
    body.structuralMass = hydro.StructuralMass(mass=100.0)

    task.model.bodies.append(body)

    file = Path("output/simo/simo_task.json")
    os.makedirs(file.parent, exist_ok=True)
    writer = SIMAWriter()
    writer.write([task], file, indent=4)


if __name__ == "__main__":
    main()
