# Generated with AreaAveragingOption
# 
from enum import Enum
from enum import auto

class AreaAveragingOption(Enum):
    """"""
    RADIAL = auto()
    CIRCULAR = auto()
    SQUARE = auto()

    def label(self):
        if self == AreaAveragingOption.RADIAL:
            return "Radial distance"
        if self == AreaAveragingOption.CIRCULAR:
            return "Circular area"
        if self == AreaAveragingOption.SQUARE:
            return "Square area"