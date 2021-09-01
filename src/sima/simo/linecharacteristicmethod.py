# Generated with LineCharacteristicMethod
# 
from enum import Enum
from enum import auto

class LineCharacteristicMethod(Enum):
    """"""
    SHOOTING = auto()
    SHOOTINGTWO = auto()
    FEM = auto()

    def label(self):
        if self == LineCharacteristicMethod.SHOOTING:
            return "Shooting"
        if self == LineCharacteristicMethod.SHOOTINGTWO:
            return "Shooting (Simplified line dynamics included)"
        if self == LineCharacteristicMethod.FEM:
            return "FEM"