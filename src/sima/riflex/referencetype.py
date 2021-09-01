# Generated with ReferenceType
# 
from enum import Enum
from enum import auto

class ReferenceType(Enum):
    """"""
    SUPER_NODE = auto()
    SUPPORT_VESSEL = auto()

    def label(self):
        if self == ReferenceType.SUPER_NODE:
            return "Super Node"
        if self == ReferenceType.SUPPORT_VESSEL:
            return "Support Vessel"