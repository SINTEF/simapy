# Generated with MultipleDeficitMethod
# 
from enum import Enum
from enum import auto

class MultipleDeficitMethod(Enum):
    """"""
    MAXOP = auto()
    DIRECT = auto()
    QUADRATIC = auto()

    def label(self):
        if self == MultipleDeficitMethod.MAXOP:
            return "MAX operator"
        if self == MultipleDeficitMethod.DIRECT:
            return "Direct summation"
        if self == MultipleDeficitMethod.QUADRATIC:
            return "Quadratic square summation"