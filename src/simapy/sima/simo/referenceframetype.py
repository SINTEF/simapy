# Generated with ReferenceFrameType
# 
from enum import Enum
from enum import auto

class ReferenceFrameType(Enum):
    """"""
    LOCAL = auto()
    GLOBAL = auto()

    def label(self):
        if self == ReferenceFrameType.LOCAL:
            return "Local"
        if self == ReferenceFrameType.GLOBAL:
            return "Global"