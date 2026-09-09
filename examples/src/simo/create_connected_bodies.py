import os
import numpy as np
from pathlib import Path
from simapy.sima import simo,hydro,sima

from simapy.sima_writer import SIMAWriter

def __create_body(name, x, y) -> simo.SIMOBody:
    bdy = simo.SIMOBody()
    bdy.name = name
    bdy.initialPosition = sima.Position(x=x,y=y)
    bp = simo.SIMOBodyPoint()
    bp.name = name + "_bp1"
    bdy.bodyPoints.append(bp)
    bdy.structuralMass = hydro.StructuralMass(mass=10.0)
    return bdy

def __create_coupling(name) -> simo.SimpleWireCoupling:
    swc = simo.SimpleWireCoupling()
    swc.name = name
    swc.ea = 10.0
    swc.length = 1.0
    return swc

if __name__ == "__main__":
    task = simo.SIMOTask()
    model = simo.SIMOModel()
    task.model=model

    nx = 6 # Number of bodies in grid x-direction
    ny = 8 # Number of bodies in grid y-direction
    dx = 10.0 # Grid Spacing in x-direction
    dy = 20.0 # Grid spacing in y-direction

    # Create bodies
    ib = 1
    for y in np.linspace(0.0, 200.0, ny):
        for x in np.linspace(0.0, 100.0, nx):
            # Copy imported body as starting point
            body = __create_body(f'Body{ib}',x,y)
            # Modify position and name
            model.bodies.append(body)
            ib += 1

    # Create couplings
    for i in range(nx - 1):
        for j in range(ny):
            idx1 = i + j * nx
            idx2 = (i + 1) + j * nx
            coupling = __create_coupling(f'cpl_{i}_{j}_1')
            coupling.endPoint1 = model.bodies[idx1].bodyPoints[0]
            coupling.endPoint2 = model.bodies[idx2].bodyPoints[0]
            model.simpleWireCouplings.append(coupling)

    for i in range(nx):
        for j in range(ny - 1):
            idx1 = i + j * nx
            idx2 = i + (j + 1) * nx
            coupling = __create_coupling(f'cpl_{i}_{j}_2')
            coupling.endPoint1 = model.bodies[idx1].bodyPoints[0]
            coupling.endPoint2 = model.bodies[idx2].bodyPoints[0]
            model.simpleWireCouplings.append(coupling)

    output = Path(__file__).parent / ".." / ".." / "output" / "simo"
    os.makedirs(output, exist_ok=True)

    # Write model to JSON file
    writer = SIMAWriter()
    writer.write([task], output / 'simotask.json')
