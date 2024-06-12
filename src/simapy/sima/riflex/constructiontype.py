# Generated with ConstructionType
# 
from enum import Enum
from enum import auto

class ConstructionType(Enum):
    """"""
    STUDLESS = auto()
    STUDLINK = auto()

    def label(self):
        if self == ConstructionType.STUDLESS:
            return "Studless"
        if self == ConstructionType.STUDLINK:
            return "StudLink"