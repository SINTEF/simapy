# Generated with FixedElongationMethod
# 
from enum import Enum
from enum import auto

class FixedElongationMethod(Enum):
    """"""
    SPRING = auto()
    CONSTANT_TENSION_WINCH = auto()

    def label(self):
        if self == FixedElongationMethod.SPRING:
            return "Spring"
        if self == FixedElongationMethod.CONSTANT_TENSION_WINCH:
            return "Constant tension winch"