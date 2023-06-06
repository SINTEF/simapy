from datetime import datetime, timedelta
import numpy as np

from simapy.sima_reader import SIMAReader
from simapy.sima_writer import SIMAWriter

from simapy.metocean import hindcast


def test_metocean_package(tmpdir):
    """Test metocean package"""
    hc = hindcast.Hindcast()
    hc.name = "Test"
    hc.description = "Test description"

    # Convert dates to string
    dates = np.arange(datetime(2021,7,1), datetime(2021,7,10), timedelta(days=1)).astype(np.datetime64)
    sdates = np.datetime_as_string(dates, unit="h", timezone="UTC").astype(str)

    hc.date = sdates
    hc.latitude = 3.0
    hc.longitude = 4.0

    current = hindcast.StochasticCurrent()
    current.name = "current"
    current.level = 100.0
    current.speed = [1.0]
    current.direction = [45.0]

    hc.current = [current]

    filename = tmpdir + '/metocean.h5'

    writer = SIMAWriter()
    writer.write([hc], filename)

    reader = SIMAReader()
    hc2 = reader.read(filename)[0]

    assert hc2.name == hc.name
