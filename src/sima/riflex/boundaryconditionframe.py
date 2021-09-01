# Generated with BoundaryConditionFrame
# 
from enum import Enum
from enum import auto

class BoundaryConditionFrame(Enum):
    """"""
    GLOBAL = auto()
    VESSEL = auto()
    SKEW_GLOBAL = auto()
    SKEW_VESSEL = auto()

    def label(self):
        if self == BoundaryConditionFrame.GLOBAL:
            return "Global"
        if self == BoundaryConditionFrame.VESSEL:
            return "Vessel"
        if self == BoundaryConditionFrame.SKEW_GLOBAL:
            return "Skew Global"
        if self == BoundaryConditionFrame.SKEW_VESSEL:
            return "Skew Vessel"