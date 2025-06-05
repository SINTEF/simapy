# Generated with UtilizationCheck
# 
from enum import Enum
from enum import auto

class UtilizationCheck(Enum):
    """"""
    TENSIONANDCURVATURE = auto()
    TENSION = auto()
    CURVATURE = auto()

    def label(self):
        if self == UtilizationCheck.TENSIONANDCURVATURE:
            return "TensionAndCurvature"
        if self == UtilizationCheck.TENSION:
            return "Tension"
        if self == UtilizationCheck.CURVATURE:
            return "Curvature"