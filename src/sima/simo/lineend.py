# Generated with LineEnd
# 
from enum import Enum
from enum import auto

class LineEnd(Enum):
    """"""
    END1 = auto()
    END2 = auto()

    def label(self):
        if self == LineEnd.END1:
            return "End 1"
        if self == LineEnd.END2:
            return "End 2"