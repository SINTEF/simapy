# Generated with WaveMethod
# 
from enum import Enum
from enum import auto

class WaveMethod(Enum):
    """"""
    NO_WAVE = auto()
    FFT_ONLY = auto()
    COSINE = auto()
    COMBINED = auto()
    VISUALIZATION = auto()

    def label(self):
        if self == WaveMethod.NO_WAVE:
            return "No wave"
        if self == WaveMethod.FFT_ONLY:
            return "FFT only"
        if self == WaveMethod.COSINE:
            return "Cosine"
        if self == WaveMethod.COMBINED:
            return "Combined"
        if self == WaveMethod.VISUALIZATION:
            return "Visualization"