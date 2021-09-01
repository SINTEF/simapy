# Generated with MassUnit
# 
from enum import Enum
from enum import auto

class MassUnit(Enum):
    """"""
    MG = auto()
    KG = auto()

    def label(self):
        if self == MassUnit.MG:
            return "Mg"
        if self == MassUnit.KG:
            return "kg"