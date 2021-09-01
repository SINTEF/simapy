# Generated with AerodynamicForceType
# 
from enum import Enum
from enum import auto

class AerodynamicForceType(Enum):
    """"""
    NONE = auto()
    AIRFOIL = auto()
    MORISON = auto()

    def label(self):
        if self == AerodynamicForceType.NONE:
            return "None"
        if self == AerodynamicForceType.AIRFOIL:
            return "Airfoil"
        if self == AerodynamicForceType.MORISON:
            return "Morison Type"