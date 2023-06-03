# Generated with WaveDriftDampingForce
# 
from enum import Enum
from enum import auto

class WaveDriftDampingForce(Enum):
    """"""
    ABSOLUTE = auto()
    RELATIVE = auto()

    def label(self):
        if self == WaveDriftDampingForce.ABSOLUTE:
            return "Absolute"
        if self == WaveDriftDampingForce.RELATIVE:
            return "Relative"