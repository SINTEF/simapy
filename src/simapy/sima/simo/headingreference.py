# Generated with HeadingReference
# 
from enum import Enum
from enum import auto

class HeadingReference(Enum):
    """"""
    TANGENTIAL = auto()
    FIXED = auto()

    def label(self):
        if self == HeadingReference.TANGENTIAL:
            return "Tangential to path"
        if self == HeadingReference.FIXED:
            return "Globally fixed"