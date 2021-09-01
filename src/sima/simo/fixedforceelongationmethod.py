# Generated with FixedForceElongationMethod
# 
from enum import Enum
from enum import auto

class FixedForceElongationMethod(Enum):
    """"""
    PRETENSION_LOCAL = auto()
    PRETENSION_GLOBAL = auto()
    BOTH_ENDS = auto()
    CONSTANT_TENSION_WINCH = auto()

    def label(self):
        if self == FixedForceElongationMethod.PRETENSION_LOCAL:
            return "Pretension and local direction"
        if self == FixedForceElongationMethod.PRETENSION_GLOBAL:
            return "Pretension and global direction"
        if self == FixedForceElongationMethod.BOTH_ENDS:
            return "Coordinates of both end points"
        if self == FixedForceElongationMethod.CONSTANT_TENSION_WINCH:
            return "Constant tension winch"