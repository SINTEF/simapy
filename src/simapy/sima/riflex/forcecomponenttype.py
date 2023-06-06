# Generated with ForceComponentType
# 
from enum import Enum
from enum import auto

class ForceComponentType(Enum):
    """"""
    CONSTANT = auto()
    HARMONIC = auto()
    RAMP = auto()

    def label(self):
        if self == ForceComponentType.CONSTANT:
            return "Constant force"
        if self == ForceComponentType.HARMONIC:
            return "Harmonic force"
        if self == ForceComponentType.RAMP:
            return "Ramp"