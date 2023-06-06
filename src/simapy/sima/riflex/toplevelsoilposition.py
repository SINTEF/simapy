# Generated with TopLevelSoilPosition
# 
from enum import Enum
from enum import auto

class TopLevelSoilPosition(Enum):
    """"""
    RELATIVE_TO_SEAFLOOR = auto()
    FIXED_DEPTH = auto()

    def label(self):
        if self == TopLevelSoilPosition.RELATIVE_TO_SEAFLOOR:
            return "Relative to seafloor"
        if self == TopLevelSoilPosition.FIXED_DEPTH:
            return "Fixed depth"