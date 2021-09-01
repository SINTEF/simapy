# Generated with FenderAttachment
# 
from enum import Enum
from enum import auto

class FenderAttachment(Enum):
    """"""
    GLOBAL_POINT = auto()
    GLOBAL_PLANE = auto()

    def label(self):
        if self == FenderAttachment.GLOBAL_POINT:
            return "Globally fixed point"
        if self == FenderAttachment.GLOBAL_PLANE:
            return "Globally fixed plane"