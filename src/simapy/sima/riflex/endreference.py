# Generated with EndReference
# 
from enum import Enum
from enum import auto

class EndReference(Enum):
    """"""
    BOTH = auto()
    ONE = auto()
    TWO = auto()

    def label(self):
        if self == EndReference.BOTH:
            return "Both"
        if self == EndReference.ONE:
            return "One"
        if self == EndReference.TWO:
            return "Two"