# Generated with BottomContactOption
# 
from enum import Enum
from enum import auto

class BottomContactOption(Enum):
    """"""
    LINE_END_ONLY = auto()
    SEAFLOOR_CONTACT = auto()

    def label(self):
        if self == BottomContactOption.LINE_END_ONLY:
            return "Line end only"
        if self == BottomContactOption.SEAFLOOR_CONTACT:
            return "Seafloor contact"