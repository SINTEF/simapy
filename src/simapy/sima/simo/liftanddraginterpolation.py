# Generated with LiftAndDragInterpolation
# 
from enum import Enum
from enum import auto

class LiftAndDragInterpolation(Enum):
    """"""
    LINEAR = auto()
    SPLINE = auto()

    def label(self):
        if self == LiftAndDragInterpolation.LINEAR:
            return "Linear"
        if self == LiftAndDragInterpolation.SPLINE:
            return "Spline"