# Generated with MassUnit
# 
from enum import Enum
from enum import auto

class MassUnit(Enum):
    """"""
    KILOGRAM = auto()
    MEGAGRAM = auto()
    POUNDS = auto()

    def label(self):
        if self == MassUnit.KILOGRAM:
            return "kg"
        if self == MassUnit.MEGAGRAM:
            return "Mg"
        if self == MassUnit.POUNDS:
            return "lbs"