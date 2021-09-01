# Generated with DampingMatrixCalculationOption
# 
from enum import Enum
from enum import auto

class DampingMatrixCalculationOption(Enum):
    """"""
    CONSTANT_PROPORTIONAL = auto()
    UPDATED_PROPORTIONAL = auto()

    def label(self):
        if self == DampingMatrixCalculationOption.CONSTANT_PROPORTIONAL:
            return "Constant proportional"
        if self == DampingMatrixCalculationOption.UPDATED_PROPORTIONAL:
            return "Updated proportional"