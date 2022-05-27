from os import path
from sima import simo
from sima import sima

from simapy.sima_writer import SIMAWriter
from simapy.sima_reader import SIMAReader


def test_that_creation_export_and_import_works(tmpdir):
    """Demonstrate how to create sima models that can be imported using the sima json model import wizard"""
    ws = sima.SIMAWorkspace()

    task = simo.SIMOTask(name = "MyTask")
    model = simo.SIMOModel()
    task.model = model
    body = simo.SIMOBody(name="body1")
    model.bodies.append(body)

    cf = sima.TaskFolder(name= "MyFolder")
    cf.childTasks.append(task)
    ws.childFolders.append(cf)

    # We will write the model to a file
    filename = tmpdir + '/test.json'
    assert not path.exists(filename)
    writer = SIMAWriter()
    writer.write([ws],filename)
    assert path.exists(filename)
    #And read it back again
    reader = SIMAReader()
    res=reader.read(filename)
    ws2 = res[0]
    assert isinstance(ws2, sima.SIMAWorkspace)
