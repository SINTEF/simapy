# Generated with BodyType
# 
from enum import Enum
from enum import auto

class BodyType(Enum):
    """"""
    PRESCRIBED = auto()
    SIX_DOF_TIME_DOMAIN = auto()
    SIX_DOF_SEPARATED_ANALYSIS = auto()
    THREE_DOF_TIME_DOMAIN = auto()

    def label(self):
        if self == BodyType.PRESCRIBED:
            return "Prescribed"
        if self == BodyType.SIX_DOF_TIME_DOMAIN:
            return "6 DOF - time domain"
        if self == BodyType.SIX_DOF_SEPARATED_ANALYSIS:
            return "6 DOF - separated analysis"
        if self == BodyType.THREE_DOF_TIME_DOMAIN:
            return "3 DOF - time domain"