# Generated with CurrentForceMethod
# 
from enum import Enum
from enum import auto

class CurrentForceMethod(Enum):
    """"""
    RELATIVE = auto()
    STATIC = auto()

    def label(self):
        if self == CurrentForceMethod.RELATIVE:
            return "Relative current velocity"
        if self == CurrentForceMethod.STATIC:
            return "Static forces only"