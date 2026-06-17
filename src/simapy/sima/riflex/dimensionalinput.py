# Generated with DimensionalInput
# 
from enum import Enum
from enum import auto

class DimensionalInput(Enum):
    """"""
    DIMENSIONAL = auto()
    NONDIMENSIONAL = auto()

    def label(self):
        if self == DimensionalInput.DIMENSIONAL:
            return "Dimensional coefficients"
        if self == DimensionalInput.NONDIMENSIONAL:
            return "Nondimensional coefficients"