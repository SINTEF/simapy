# Generated with GDFType
# 
from enum import Enum
from enum import auto

class GDFType(Enum):
    """"""
    BODY = auto()
    LID = auto()
    CONTROL = auto()

    def label(self):
        if self == GDFType.BODY:
            return "Body Surface"
        if self == GDFType.LID:
            return "Lid Surface"
        if self == GDFType.CONTROL:
            return "Control Surface"