# Generated with PeakExtreme
# 
from enum import Enum
from enum import auto

class PeakExtreme(Enum):
    """"""
    MAX = auto()
    MIN = auto()

    def label(self):
        if self == PeakExtreme.MAX:
            return "Maxima"
        if self == PeakExtreme.MIN:
            return "Minima"