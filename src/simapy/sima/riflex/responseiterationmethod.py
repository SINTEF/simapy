# Generated with ResponseIterationMethod
# 
from enum import Enum
from enum import auto

class ResponseIterationMethod(Enum):
    """"""
    FIXED_POINT = auto()
    NEWTON_RAPHSON = auto()

    def label(self):
        if self == ResponseIterationMethod.FIXED_POINT:
            return "Fixed point"
        if self == ResponseIterationMethod.NEWTON_RAPHSON:
            return "Newton-Raphson"