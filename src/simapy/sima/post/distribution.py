# Generated with Distribution
# 
from enum import Enum
from enum import auto

class Distribution(Enum):
    """"""
    RAYLEIGH = auto()
    WEIBULL = auto()
    GUMBEL = auto()

    def label(self):
        if self == Distribution.RAYLEIGH:
            return "Rayleigh"
        if self == Distribution.WEIBULL:
            return "Weibull"
        if self == Distribution.GUMBEL:
            return "Gumbel"