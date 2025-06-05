# Generated with WamitWaveForceOption
# 
from enum import Enum
from enum import auto

class WamitWaveForceOption(Enum):
    """"""
    DIFFRACTION = auto()
    HASKIND = auto()

    def label(self):
        if self == WamitWaveForceOption.DIFFRACTION:
            return "Diffraction"
        if self == WamitWaveForceOption.HASKIND:
            return "Haskind"