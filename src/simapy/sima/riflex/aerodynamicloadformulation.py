# Generated with AerodynamicLoadFormulation
# 
from enum import Enum
from enum import auto

class AerodynamicLoadFormulation(Enum):
    """"""
    NONE = auto()
    DRAG = auto()
    TDVIV = auto()

    def label(self):
        if self == AerodynamicLoadFormulation.NONE:
            return "None"
        if self == AerodynamicLoadFormulation.DRAG:
            return "Morison drag"
        if self == AerodynamicLoadFormulation.TDVIV:
            return "Time domain VIV"