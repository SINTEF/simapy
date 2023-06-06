# Generated with NonlinearBuoyancyCorrectionMethod
# 
from enum import Enum
from enum import auto

class NonlinearBuoyancyCorrectionMethod(Enum):
    """"""
    MWL = auto()
    WAVE = auto()

    def label(self):
        if self == NonlinearBuoyancyCorrectionMethod.MWL:
            return "Mean water level"
        if self == NonlinearBuoyancyCorrectionMethod.WAVE:
            return "Wave"