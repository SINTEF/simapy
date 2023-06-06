# Generated with DOF
# 
from enum import Enum
from enum import auto

class DOF(Enum):
    """"""
    X = auto()
    Y = auto()
    Z = auto()
    RX = auto()
    RY = auto()
    RZ = auto()

    def label(self):
        if self == DOF.X:
            return "X"
        if self == DOF.Y:
            return "Y"
        if self == DOF.Z:
            return "Z"
        if self == DOF.RX:
            return "Rx"
        if self == DOF.RY:
            return "Ry"
        if self == DOF.RZ:
            return "Rz"