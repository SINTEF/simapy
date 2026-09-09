"""
This file will be called from a SIMA workflow
Use generate_workflow.py to generate a json file that can be imported into SIMA
"""
import sys
from random import random

import numpy as np
from simapy.sima.signals.container import Container
from simapy.sima.signals.dimensionalscalar import DimensionalScalar
from simapy.sima.signals.equallyspacedsignal import EquallySpacedSignal
from simapy.sima_reader import SIMAReader
from simapy.sima_writer import SIMAWriter

# The first argument is the path to this file
# check for additional input argument
num = 10 * random()
if len(sys.argv) > 1:
    num = float(sys.argv[1])

sima_reader = SIMAReader()

file = "in.json"
items = sima_reader.read(file)
container: Container = items[0]
signals = container.signals
timeseries: EquallySpacedSignal = container.signals[0]
timeseries.name = timeseries.name + "_frompy"
multiplied = np.multiply(np.array(timeseries.value), num)
timeseries.value = multiplied.tolist()

mynum: DimensionalScalar = container.signals[1]
mynum.name = mynum.name + "_frompy"
mynum.value = mynum.value * num

writer = SIMAWriter()
writer.write([container], "out.json")
