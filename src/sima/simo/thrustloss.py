# Generated with ThrustLoss
# 
from enum import Enum
from enum import auto

class ThrustLoss(Enum):
    """"""
    NONE = auto()
    SURFACE = auto()

    def label(self):
        if self == ThrustLoss.NONE:
            return "None"
        if self == ThrustLoss.SURFACE:
            return "Surface"