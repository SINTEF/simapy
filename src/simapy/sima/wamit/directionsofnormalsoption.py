# Generated with DirectionsOfNormalsOption
# 
from enum import Enum
from enum import auto

class DirectionsOfNormalsOption(Enum):
    """"""
    OUTWARD = auto()
    INWARD = auto()

    def label(self):
        if self == DirectionsOfNormalsOption.OUTWARD:
            return "Outward"
        if self == DirectionsOfNormalsOption.INWARD:
            return "Inward"