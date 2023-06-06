# Generated with WaveAmplitudeComputation
# 
from enum import Enum
from enum import auto

class WaveAmplitudeComputation(Enum):
    """"""
    DETERMINISTIC = auto()
    STOCHASTIC = auto()

    def label(self):
        if self == WaveAmplitudeComputation.DETERMINISTIC:
            return "Deterministic"
        if self == WaveAmplitudeComputation.STOCHASTIC:
            return "Stochastic"