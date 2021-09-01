# Generated with IEC2005WindEventType
# 
from enum import Enum
from enum import auto

class IEC2005WindEventType(Enum):
    """"""
    ECD = auto()
    EWSV = auto()
    EWSH = auto()
    EOG = auto()
    EDC = auto()

    def label(self):
        if self == IEC2005WindEventType.ECD:
            return "Extreme coherent gust with direction change - ECD"
        if self == IEC2005WindEventType.EWSV:
            return "Extreme vertical wind shear - EWSV"
        if self == IEC2005WindEventType.EWSH:
            return "Extreme horizontal wind shear - EWSH"
        if self == IEC2005WindEventType.EOG:
            return "Extreme operating gust - EOG"
        if self == IEC2005WindEventType.EDC:
            return "Extreme direction change - EDC"