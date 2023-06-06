# Generated with WaveTheory
# 
from enum import Enum
from enum import auto

class WaveTheory(Enum):
    """"""
    AIRY_LINEAR = auto()
    STOKE_5TH_ORDER = auto()

    def label(self):
        if self == WaveTheory.AIRY_LINEAR:
            return "Airy linear"
        if self == WaveTheory.STOKE_5TH_ORDER:
            return "Stoke 5th order"