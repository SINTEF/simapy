# Generated with ConvergenceNorm
# 
from enum import Enum
from enum import auto

class ConvergenceNorm(Enum):
    """"""
    DISP = auto()
    BOTH = auto()

    def label(self):
        if self == ConvergenceNorm.DISP:
            return "Displacement"
        if self == ConvergenceNorm.BOTH:
            return "Both"