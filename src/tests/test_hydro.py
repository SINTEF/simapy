from sima.simo import SIMOModel,SIMOBody,SIMOTask
from sima.hydro import FirstOrderMotionTransferFunction, DirectionDependentComplexValues, ComplexValues
from simapy.sima_writer import SIMAWriter
from simapy.sima_reader import SIMAReader

def test_hydro_creation(tmpdir):
    body = SIMOBody(name='body1')
    rao = FirstOrderMotionTransferFunction()
    rao.frequencies = [0.1, 0.2, 0.3, 0.4]
    rao.directions = [0.0, 45.0, 180.0]

    dir1 = ComplexValues(
        realValues = [1.0, 2.0, 3.0, 4.0],
        imagValues = [2.0, 3.0, 4.0, 5.0]
    )
    dir2 = ComplexValues(
        realValues = [5.0, 6.0, 7.0, 8.0],
        imagValues = [10.0, 11.0, 12.0, 13.0]
    )
    dir3 = ComplexValues(
        realValues = [14.0, 15.0, 16.0, 17.0],
        imagValues = [18.0, 19.0, 20.0, 21.0]
    )
    rao.surge = DirectionDependentComplexValues(
        directionalValues = [dir1, dir2, dir3]
    )

    body.firstOrderMotionTransferFunction = rao
    task = SIMOTask(name='HydroImport')
    model = SIMOModel()
    task.model = model
    model.bodies.append(body)
    filename = tmpdir + '/hydro.json'
    writer = SIMAWriter()
    writer.write([task], filename)

    reader = SIMAReader()
    res=reader.read(filename)
    task2 = res[0]
    assert isinstance(task2, SIMOTask)
