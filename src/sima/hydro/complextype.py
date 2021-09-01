# Generated with ComplexType
# 
from enum import Enum
from enum import auto

class ComplexType(Enum):
    """"""
    REAL_IMAG = auto()
    AMP_DEG_PHASE = auto()
    AMP_RAD_PHASE = auto()

    def label(self):
        if self == ComplexType.REAL_IMAG:
            return "Complex"
        if self == ComplexType.AMP_DEG_PHASE:
            return "Amplitude Phase [deg]"
        if self == ComplexType.AMP_RAD_PHASE:
            return "Amplitude Phase [rad]"