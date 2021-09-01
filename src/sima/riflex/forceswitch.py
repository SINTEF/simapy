# Generated with ForceSwitch
# 
from enum import Enum
from enum import auto

class ForceSwitch(Enum):
    """"""
    USE_STIFFNESS_MATRIX = auto()
    USE_CURVATURE = auto()

    def label(self):
        if self == ForceSwitch.USE_STIFFNESS_MATRIX:
            return "Use stiffness matrix"
        if self == ForceSwitch.USE_CURVATURE:
            return "Use curvature"