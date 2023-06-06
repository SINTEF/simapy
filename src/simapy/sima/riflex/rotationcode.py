# Generated with RotationCode
# 
from enum import Enum
from enum import auto

class RotationCode(Enum):
    """"""
    NONE = auto()
    X_AXIS = auto()
    Y_AXIS = auto()
    Z_AXIS = auto()

    def label(self):
        if self == RotationCode.NONE:
            return "No rotation"
        if self == RotationCode.X_AXIS:
            return "Rotation about x-axis"
        if self == RotationCode.Y_AXIS:
            return "Rotation about y-axis"
        if self == RotationCode.Z_AXIS:
            return "Rotation about z-axis"