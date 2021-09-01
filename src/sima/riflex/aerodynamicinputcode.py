# Generated with AerodynamicInputCode
# 
from enum import Enum
from enum import auto

class AerodynamicInputCode(Enum):
    """"""
    NONE = auto()
    DIMENSIONAL = auto()
    NONDIMENSIONAL = auto()

    def label(self):
        if self == AerodynamicInputCode.NONE:
            return "None"
        if self == AerodynamicInputCode.DIMENSIONAL:
            return "Dimensional coefficients"
        if self == AerodynamicInputCode.NONDIMENSIONAL:
            return "Nondimensional coefficients"