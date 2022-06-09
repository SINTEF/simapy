# Generated with TurbineDirection
# 
from enum import Enum
from enum import auto

class TurbineDirection(Enum):
    """"""
    UPWIND = auto()
    DOWNWIND = auto()

    def label(self):
        if self == TurbineDirection.UPWIND:
            return "Upwind"
        if self == TurbineDirection.DOWNWIND:
            return "Downwind"