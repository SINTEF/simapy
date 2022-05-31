from sima import simo
from sima import hydro
from simapy.sima_writer import SIMAWriter
from simapy.sima_reader import SIMAReader

def test_hydro_creation(tmpdir):
    """Creates a First Order Motion Transfer function"""
    body = simo.SIMOBody(name='body1')
    rao = hydro.FirstOrderMotionTransferFunction()
    rao.frequencies = [0.1, 0.2, 0.3, 0.4]
    rao.directions = [0.0, 45.0, 180.0]

    dir1 = hydro.ComplexValues(
        realValues = [1.0, 2.0, 3.0, 4.0],
        imagValues = [2.0, 3.0, 4.0, 5.0]
    )
    dir2 = hydro.ComplexValues(
        realValues = [5.0, 6.0, 7.0, 8.0],
        imagValues = [10.0, 11.0, 12.0, 13.0]
    )
    dir3 = hydro.ComplexValues(
        realValues = [14.0, 15.0, 16.0, 17.0],
        imagValues = [18.0, 19.0, 20.0, 21.0]
    )
    rao.surge = hydro.DirectionDependentComplexValues(
        directionalValues = [dir1, dir2, dir3]
    )

    body.firstOrderMotionTransferFunction = rao
    task = simo.SIMOTask(name='HydroImport')
    model = simo.SIMOModel()
    task.model = model
    model.bodies.append(body)
    filename = tmpdir + '/hydro.json'
    writer = SIMAWriter()
    writer.write([task], filename)

    reader = SIMAReader()
    res=reader.read(filename)
    task2 = res[0]
    assert isinstance(task2, simo.SIMOTask)
