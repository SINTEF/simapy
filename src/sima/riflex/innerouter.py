# Generated with InnerOuter
# 
from enum import Enum
from enum import auto

class InnerOuter(Enum):
    """"""
    INNER = auto()
    OUTER = auto()

    def label(self):
        if self == InnerOuter.INNER:
            return "Inner"
        if self == InnerOuter.OUTER:
            return "Outer"