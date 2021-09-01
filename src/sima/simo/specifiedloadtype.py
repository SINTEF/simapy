# Generated with SpecifiedLoadType
# 
from enum import Enum
from enum import auto

class SpecifiedLoadType(Enum):
    """"""
    CONSTANT = auto()
    HARMONIC = auto()
    RAMP = auto()

    def label(self):
        if self == SpecifiedLoadType.CONSTANT:
            return "Constant"
        if self == SpecifiedLoadType.HARMONIC:
            return "Harmonic"
        if self == SpecifiedLoadType.RAMP:
            return "Ramp"