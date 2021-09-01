# Generated with IECWindProfileType
# 
from enum import Enum
from enum import auto

class IECWindProfileType(Enum):
    """"""
    LOG = auto()
    PL = auto()

    def label(self):
        if self == IECWindProfileType.LOG:
            return "Logarithmic"
        if self == IECWindProfileType.PL:
            return "Power law"