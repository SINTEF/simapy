# Generated with AxialStiffness
# 
from enum import Enum
from enum import auto

class AxialStiffness(Enum):
    """"""
    CONSTANT = auto()
    TENSION_ELONGATION = auto()

    def label(self):
        if self == AxialStiffness.CONSTANT:
            return "Constant"
        if self == AxialStiffness.TENSION_ELONGATION:
            return "Tension-elongation"