# Generated with CompensatorLimitation
# 
from enum import Enum
from enum import auto

class CompensatorLimitation(Enum):
    """"""
    FACTOR = auto()
    FACTOR_AMAX = auto()
    AMAX = auto()

    def label(self):
        if self == CompensatorLimitation.FACTOR:
            return "Factor limit"
        if self == CompensatorLimitation.FACTOR_AMAX:
            return "Factor amax limit"
        if self == CompensatorLimitation.AMAX:
            return "Amax limit"