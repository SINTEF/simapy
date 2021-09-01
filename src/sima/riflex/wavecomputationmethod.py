# Generated with WaveComputationMethod
# 
from enum import Enum
from enum import auto

class WaveComputationMethod(Enum):
    """"""
    FFT = auto()
    COS = auto()
    WF2D = auto()

    def label(self):
        if self == WaveComputationMethod.FFT:
            return "FFT (Prestochastic analysis)"
        if self == WaveComputationMethod.COS:
            return "Cos series"
        if self == WaveComputationMethod.WF2D:
            return "2D wave field"