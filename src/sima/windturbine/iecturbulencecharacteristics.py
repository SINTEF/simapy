# Generated with IECTurbulenceCharacteristics
# 
from enum import Enum
from enum import auto

class IECTurbulenceCharacteristics(Enum):
    """"""
    A = auto()
    B = auto()
    C = auto()
    PERCENT = auto()

    def label(self):
        if self == IECTurbulenceCharacteristics.A:
            return "A"
        if self == IECTurbulenceCharacteristics.B:
            return "B"
        if self == IECTurbulenceCharacteristics.C:
            return "C"
        if self == IECTurbulenceCharacteristics.PERCENT:
            return "In percent"