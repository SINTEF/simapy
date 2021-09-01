# Generated with PowerExtraction
# 
from enum import Enum
from enum import auto

class PowerExtraction(Enum):
    """"""
    POWER = auto()
    TORQUE = auto()

    def label(self):
        if self == PowerExtraction.POWER:
            return "Constant Power"
        if self == PowerExtraction.TORQUE:
            return "Constant Torque"