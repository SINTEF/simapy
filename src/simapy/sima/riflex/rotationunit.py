# Generated with RotationUnit
# 
from enum import Enum
from enum import auto

class RotationUnit(Enum):
    """"""
    DEGR = auto()
    RADI = auto()

    def label(self):
        if self == RotationUnit.DEGR:
            return "Degrees"
        if self == RotationUnit.RADI:
            return "Radians"