# Generated with MethodIndicator
# 
from enum import Enum
from enum import auto

class MethodIndicator(Enum):
    """"""
    NONLINEAR = auto()
    LINEAR = auto()

    def label(self):
        if self == MethodIndicator.NONLINEAR:
            return "Nonlinear"
        if self == MethodIndicator.LINEAR:
            return "Linear"