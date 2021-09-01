# Generated with WindVelocityDimension
# 
from enum import Enum
from enum import auto

class WindVelocityDimension(Enum):
    """"""
    TWO = auto()
    ONE = auto()

    def label(self):
        if self == WindVelocityDimension.TWO:
            return "Two dimensional"
        if self == WindVelocityDimension.ONE:
            return "One dimensional"