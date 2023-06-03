# Generated with MassSummaryReference
# 
from enum import Enum
from enum import auto

class MassSummaryReference(Enum):
    """"""
    BODY = auto()
    COORDINATES = auto()

    def label(self):
        if self == MassSummaryReference.BODY:
            return "BODY"
        if self == MassSummaryReference.COORDINATES:
            return "COORDINATES"