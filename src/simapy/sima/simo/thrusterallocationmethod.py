# Generated with ThrusterAllocationMethod
# 
from enum import Enum
from enum import auto

class ThrusterAllocationMethod(Enum):
    """"""
    ORDINARY = auto()
    HEADING = auto()

    def label(self):
        if self == ThrusterAllocationMethod.ORDINARY:
            return "Ordinary allocation"
        if self == ThrusterAllocationMethod.HEADING:
            return "Heading priority"