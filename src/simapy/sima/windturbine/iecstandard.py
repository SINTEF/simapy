# Generated with IECStandard
# 
from enum import Enum
from enum import auto

class IECStandard(Enum):
    """"""
    IEC_61400_1 = auto()
    IEC_61400_1_ED2 = auto()
    IEC_61400_2 = auto()
    IEC_61400_3 = auto()

    def label(self):
        if self == IECStandard.IEC_61400_1:
            return "IEC 61400-1"
        if self == IECStandard.IEC_61400_1_ED2:
            return "IEC 61400-1 Ed2"
        if self == IECStandard.IEC_61400_2:
            return "IEC 61400-2"
        if self == IECStandard.IEC_61400_3:
            return "IEC 61400-3"