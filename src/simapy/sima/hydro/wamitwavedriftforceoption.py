# Generated with WamitWaveDriftForceOption
# 
from enum import Enum
from enum import auto

class WamitWaveDriftForceOption(Enum):
    """"""
    MOMENTUM = auto()
    PRESSURE = auto()
    CONTROL_SURFACE = auto()

    def label(self):
        if self == WamitWaveDriftForceOption.MOMENTUM:
            return "Momentum"
        if self == WamitWaveDriftForceOption.PRESSURE:
            return "Pressure"
        if self == WamitWaveDriftForceOption.CONTROL_SURFACE:
            return "Control surface"