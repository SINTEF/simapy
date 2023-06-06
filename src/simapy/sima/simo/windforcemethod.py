# Generated with WindForceMethod
# 
from enum import Enum
from enum import auto

class WindForceMethod(Enum):
    """"""
    RELATIVE = auto()
    STATIC = auto()
    ABSOLUTE = auto()

    def label(self):
        if self == WindForceMethod.RELATIVE:
            return "Relative wind velocity"
        if self == WindForceMethod.STATIC:
            return "Static forces only"
        if self == WindForceMethod.ABSOLUTE:
            return "Absolute wind velocity"