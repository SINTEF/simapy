# Generated with SlugForceDensityControl
# 
from enum import Enum
from enum import auto

class SlugForceDensityControl(Enum):
    """"""
    CONSTANT = auto()
    VARIABLE = auto()

    def label(self):
        if self == SlugForceDensityControl.CONSTANT:
            return "Constant density"
        if self == SlugForceDensityControl.VARIABLE:
            return "Variable density with vertical position"