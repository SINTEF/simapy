# Generated with Formulation
# 
from enum import Enum
from enum import auto

class Formulation(Enum):
    """"""
    SIMO_41 = auto()
    SIMO_40 = auto()

    def label(self):
        if self == Formulation.SIMO_41:
            return "SIMO 4.1"
        if self == Formulation.SIMO_40:
            return "SIMO 4.0"