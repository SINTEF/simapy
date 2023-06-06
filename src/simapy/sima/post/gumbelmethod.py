# Generated with GumbelMethod
# 
from enum import Enum
from enum import auto

class GumbelMethod(Enum):
    """"""
    LSQ = auto()
    MOMENT = auto()

    def label(self):
        if self == GumbelMethod.LSQ:
            return "Least Square Fit"
        if self == GumbelMethod.MOMENT:
            return "Moment"