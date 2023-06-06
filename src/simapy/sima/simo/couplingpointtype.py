# Generated with CouplingPointType
# 
from enum import Enum
from enum import auto

class CouplingPointType(Enum):
    """"""
    FIXED = auto()
    GUIDE = auto()

    def label(self):
        if self == CouplingPointType.FIXED:
            return "Fixed"
        if self == CouplingPointType.GUIDE:
            return "Guide"