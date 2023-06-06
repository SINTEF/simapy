# Generated with End
# 
from enum import Enum
from enum import auto

class End(Enum):
    """"""
    ONE = auto()
    TWO = auto()

    def label(self):
        if self == End.ONE:
            return "End 1"
        if self == End.TWO:
            return "End 2"