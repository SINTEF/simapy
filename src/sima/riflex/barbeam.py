# Generated with BarBeam
# 
from enum import Enum
from enum import auto

class BarBeam(Enum):
    """"""
    BAR = auto()
    BEAM = auto()

    def label(self):
        if self == BarBeam.BAR:
            return "Bar"
        if self == BarBeam.BEAM:
            return "Beam"