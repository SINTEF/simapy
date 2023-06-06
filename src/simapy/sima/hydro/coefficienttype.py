# Generated with CoefficientType
# 
from enum import Enum
from enum import auto

class CoefficientType(Enum):
    """"""
    CLASSIC = auto()
    ADVANCED = auto()

    def label(self):
        if self == CoefficientType.CLASSIC:
            return "Classic"
        if self == CoefficientType.ADVANCED:
            return "Position dependent"