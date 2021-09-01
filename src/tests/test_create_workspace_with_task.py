from sima.simo import SIMOModel,SIMOBody,SIMOTask
from sima.sima import SIMAWorkspace, TaskFolder

from simapy.sima_writer import SIMAWriter
from simapy.sima_reader import SIMAReader

from os import path

def test_that_creation_export_and_import_works(tmpdir):
    """Demonstrate how to create sima models that can be imported using the sima json model import wizard"""
    ws = SIMAWorkspace()

    task = SIMOTask(name = "MyTask")
    model = SIMOModel()
    task.model = model
    body = SIMOBody(name="body1")
    model.bodies.append(body)

    cf = TaskFolder(name= "MyFolder")
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
    assert isinstance(ws2, SIMAWorkspace)
