# Generated with TurbineOrientation
# 
from enum import Enum
from enum import auto

class TurbineOrientation(Enum):
    """"""
    UPWIND = auto()
    DOWNWIND = auto()

    def label(self):
        if self == TurbineOrientation.UPWIND:
            return "Upwind"
        if self == TurbineOrientation.DOWNWIND:
            return "Downwind"