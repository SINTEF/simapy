# Generated with Focus
# 
from enum import Enum
from enum import auto

class Focus(Enum):
    """"""
    TARGET = auto()
    PARK = auto()

    def label(self):
        if self == Focus.TARGET:
            return "Target"
        if self == Focus.PARK:
            return "Park"