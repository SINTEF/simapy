# Generated with HydrodynamicInputCode
# 
from enum import Enum
from enum import auto

class HydrodynamicInputCode(Enum):
    """"""
    DIMENSIONAL = auto()
    NONDIMENSIONAL = auto()

    def label(self):
        if self == HydrodynamicInputCode.DIMENSIONAL:
            return "Dimensional coefficients"
        if self == HydrodynamicInputCode.NONDIMENSIONAL:
            return "Nondimensional coefficients"