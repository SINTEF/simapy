from os import path
from marmo.containers.container import Container
from marmo.containers.dimensionalscalar import DimensionalScalar
from marmo.containers.equallyspacedsignal import EquallySpacedSignal
from marmo.containers.nonequallyspacedsignal import NonEquallySpacedSignal
from simapy.sima_writer import SIMAWriter

from math import sin

def test_signal_creation(tmpdir):
    """Demonstrates how to create signals that can go straight into a sima post processor or workflow"""
    container = Container(name = "Top")
    container.signals.append(__create_scalar())

    child = Container(name="child")
    child.signals.append(__create_equally_spaced())
    child.signals.append(__create_non_equally_spaced())

    filename = tmpdir + '/signals.json'
    SIMAWriter().write([container],filename)
    assert path.exists(filename)

def __create_scalar() -> DimensionalScalar:
    scalar = DimensionalScalar()
    scalar.name = "myScalar"
    scalar.unit = "-"
    scalar.value = 42.0
    return scalar

def __create_equally_spaced() -> EquallySpacedSignal:
    # EqualySpacedSignals x-axis is defined by xstart and xdelta
    force = EquallySpacedSignal()
    force.name = "force"
    # Y-axis unit
    force.unit = "N"
    force.xunit = "s"
    # We will create a sine curce with a sample time of 0.1 seconds
    dt = 0.1
    omega = 1
    force.value = [sin(omega*dt*float(i)) for i in range(1, 100)]
    # The time series starts at 10 seconds
    force.xstart = 10.0
    force.xdelta = dt
    return force

def __create_non_equally_spaced() -> NonEquallySpacedSignal:
    # NonEqualySpacedSignals has both x and y axis defined
    xy = NonEquallySpacedSignal()
    xy.name = "xy"
    # Y-axis unit
    xy.unit = "N"
    xy.xunit = "m"
    xy.xvalue = [10.0, 12.0, 17.0]
    xy.value = [10.0, 1.0, 5.0]
    return xy

