# Generated with WaveIntegrationMethod
# 
from enum import Enum
from enum import auto

class WaveIntegrationMethod(Enum):
    """"""
    ACTUAL_WAVE_ELEVATION = auto()
    STRICTLY_LINEAR_WAVE = auto()

    def label(self):
        if self == WaveIntegrationMethod.ACTUAL_WAVE_ELEVATION:
            return "Actual wave elevation"
        if self == WaveIntegrationMethod.STRICTLY_LINEAR_WAVE:
            return "Strictly linear wave"