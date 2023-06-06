# Generated with SegmentType
# 
from enum import Enum
from enum import auto

class SegmentType(Enum):
    """"""
    CATENARY = auto()
    RIGID = auto()

    def label(self):
        if self == SegmentType.CATENARY:
            return "Catenary"
        if self == SegmentType.RIGID:
            return "Rigid"