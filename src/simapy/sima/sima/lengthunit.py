# Generated with LengthUnit
# 
from enum import Enum
from enum import auto

class LengthUnit(Enum):
    """"""
    METER = auto()
    FEET = auto()
    MILLIMETER = auto()

    def label(self):
        if self == LengthUnit.METER:
            return "m"
        if self == LengthUnit.FEET:
            return "ft"
        if self == LengthUnit.MILLIMETER:
            return "mm"