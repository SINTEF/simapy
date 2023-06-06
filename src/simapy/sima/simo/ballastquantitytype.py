# Generated with BallastQuantityType
# 
from enum import Enum
from enum import auto

class BallastQuantityType(Enum):
    """"""
    PERCENTAGE = auto()
    VOLUME = auto()

    def label(self):
        if self == BallastQuantityType.PERCENTAGE:
            return "%"
        if self == BallastQuantityType.VOLUME:
            return "m^3"