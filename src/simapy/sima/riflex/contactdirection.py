# Generated with ContactDirection
# 
from enum import Enum
from enum import auto

class ContactDirection(Enum):
    """"""
    INWARDS = auto()
    OUTWARDS = auto()

    def label(self):
        if self == ContactDirection.INWARDS:
            return "Inwards"
        if self == ContactDirection.OUTWARDS:
            return "Outwards"