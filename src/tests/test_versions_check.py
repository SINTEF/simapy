import json
from simapy.sima import simo
from simapy.sima_reader import SIMAReader
from simapy.sima_writer import SIMAWriter


def test_version_check(tmpdir):
    """ Test that version check works when package version is different """
    task = simo.SIMOTask()
    file = tmpdir + '/test.json'
    SIMAWriter().write([task], file)

    # Read the file again to see that it works fine
    task2 = SIMAReader().read(file)[0]
    assert task2.name == task.name
    # Now lets tamper with the file
    with open(file, 'r',encoding="utf8") as f:
        data = json.load(f)
        pkg = data['header']['packages'][0]
        current = pkg['version']
        pkg['version'] = current + 1

    with open(file, 'w',encoding="utf8") as f:
        json.dump(data, f)

    # Now we should get an error
    try:
        SIMAReader().read(file)
        assert False
    except ValueError as e:
        expected = f'Package {pkg["name"]} has version {current+1} but reader expects {current}'
        assert expected  in str(e)
