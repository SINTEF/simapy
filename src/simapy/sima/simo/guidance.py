# Generated with Guidance
# 
from enum import Enum
from enum import auto

class Guidance(Enum):
    """"""
    STRAIGHT_LINES = auto()
    LOS = auto()

    def label(self):
        if self == Guidance.STRAIGHT_LINES:
            return "Straight lines and circular arcs"
        if self == Guidance.LOS:
            return "Line of sight (LOS)"