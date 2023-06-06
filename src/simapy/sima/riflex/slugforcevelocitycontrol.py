# Generated with SlugForceVelocityControl
# 
from enum import Enum
from enum import auto

class SlugForceVelocityControl(Enum):
    """"""
    CONSTANT = auto()
    VARIABLE = auto()

    def label(self):
        if self == SlugForceVelocityControl.CONSTANT:
            return "Constant velocity"
        if self == SlugForceVelocityControl.VARIABLE:
            return "Variable velocity"