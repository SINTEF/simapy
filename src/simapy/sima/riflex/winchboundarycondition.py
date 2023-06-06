# Generated with WinchBoundaryCondition
# 
from enum import Enum
from enum import auto

class WinchBoundaryCondition(Enum):
    """"""
    FIXED = auto()
    VESSEL = auto()
    FLOATE = auto()

    def label(self):
        if self == WinchBoundaryCondition.FIXED:
            return "Fixed boundaries"
        if self == WinchBoundaryCondition.VESSEL:
            return "Attached to support vessel"
        if self == WinchBoundaryCondition.FLOATE:
            return "Attached to SIMO body"