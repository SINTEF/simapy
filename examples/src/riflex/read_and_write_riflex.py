"""Read and Write RIFLEX Models.

This example demonstrates how to manipulate RIFLEX models programmatically using the SIMAPy API.

The example includes:
    1. Importing an existing RIFLEX model from a JSON file (exported from SIMA)
    2. Using the first line in the model as a template
    3. Creating multiple new lines with randomized positions
    4. Exporting the modified model back to a JSON file that can be imported into SIMA

    >>> python read_and_write_riflex.py
"""

import os
from pathlib import Path
from random import random

from simapy.sima.riflex.riflextask import RIFLEXTask
from simapy.sima.riflex.supernode import SuperNode
from simapy.sima_reader import SIMAReader
from simapy.sima_writer import SIMAWriter


def __copy_and_move(sn: SuperNode, offset):
    """
    Copy a SuperNode and move the copy with the given offset.
    
    This helper function creates a copy of a SuperNode and applies a position
    offset to both the initial and static positions in the x and y coordinates.
    
    Args:
        sn (SuperNode): The source SuperNode to copy
        offset (float): The offset distance to apply to x and y coordinates
        
    Returns:
        SuperNode: A new SuperNode with the offset applied
    """
    sn_copy = sn.copy()
    sn_copy.xInitial = sn_copy.xInitial + offset
    sn_copy.yInitial = sn_copy.yInitial + offset
    sn_copy.xStatic = sn_copy.xStatic + offset
    sn_copy.yStatic = sn_copy.yStatic + offset
    return sn_copy

def main():
    """Main function to execute the RIFLEX model example."""
    reader = SIMAReader()
    root = Path(__file__).parent / ".." / ".."
    input = root / "input"
    contents = reader.read(input / "riflex" / "simple_flexible_riser.json")
    # Using type hints is not necessary but is useful to get automatic help when using an IDE, such as vscode or pycharm
    task: RIFLEXTask = contents[0]
    # We will use the first line as a template to generate new ones
    model = task.model
    lines = model.slenderSystem.lines
    nodes = model.slenderSystem.superNodes
    line = lines[0]

    for name in ["line_1", "line_2", "line_3"]:
        line_i = line.copy()
        line_i.name = name
        # create two new nodes and move to random position
        end_offset = 300.0 * random()

        sn_end_1: SuperNode = __copy_and_move(line_i.end1, end_offset)
        sn_end_1.name = name + "_end1"
        line_i.end1 = sn_end_1
        nodes.append(sn_end_1)

        sn_end_2: SuperNode = __copy_and_move(line_i.end2, end_offset)
        sn_end_2.name = name + "_end2"
        line_i.end2 = sn_end_2
        nodes.append(sn_end_2)

        lines.append(line_i)

    file = root / "output/riflex/simple_flexible_riser_mod.json"
    os.makedirs(file.parent, exist_ok=True)
    writer = SIMAWriter()
    writer.write([task], file)


if __name__ == "__main__":
    main()
