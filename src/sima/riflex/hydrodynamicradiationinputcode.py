# Generated with HydrodynamicRadiationInputCode
# 
from enum import Enum
from enum import auto

class HydrodynamicRadiationInputCode(Enum):
    """"""
    DIMENSIONAL = auto()
    NONDIMENSIONAL = auto()

    def label(self):
        if self == HydrodynamicRadiationInputCode.DIMENSIONAL:
            return "Dimensional coefficients"
        if self == HydrodynamicRadiationInputCode.NONDIMENSIONAL:
            return "Nondimensional coefficients"