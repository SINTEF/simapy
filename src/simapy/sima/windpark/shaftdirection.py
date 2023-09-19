# Generated with ShaftDirection
# 
from enum import Enum
from enum import auto

class ShaftDirection(Enum):
    """"""
    POSI = auto()
    YAW = auto()

    def label(self):
        if self == ShaftDirection.POSI:
            return "Global XY plane"
        if self == ShaftDirection.YAW:
            return "Yaw misalignment"