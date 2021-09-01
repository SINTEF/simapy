# Generated with ResponseAmount
# 
from enum import Enum
from enum import auto

class ResponseAmount(Enum):
    """"""
    MIN = auto()
    MED = auto()
    MAX = auto()

    def label(self):
        if self == ResponseAmount.MIN:
            return "Minimum"
        if self == ResponseAmount.MED:
            return "Medium"
        if self == ResponseAmount.MAX:
            return "Maximum"