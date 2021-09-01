# Generated with TangentialFroudeKrylovScaling
# 
from enum import Enum
from enum import auto

class TangentialFroudeKrylovScaling(Enum):
    """"""
    ON = auto()
    OFF = auto()

    def label(self):
        if self == TangentialFroudeKrylovScaling.ON:
            return "On"
        if self == TangentialFroudeKrylovScaling.OFF:
            return "Off"