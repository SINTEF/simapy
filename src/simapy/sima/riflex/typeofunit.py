# Generated with TypeOfUnit
# 
from enum import Enum
from enum import auto

class TypeOfUnit(Enum):
    """"""
    PERMANENT = auto()
    MOBILE = auto()
    PERMANENTANDMOBILE = auto()

    def label(self):
        if self == TypeOfUnit.PERMANENT:
            return "Permanent"
        if self == TypeOfUnit.MOBILE:
            return "Mobile"
        if self == TypeOfUnit.PERMANENTANDMOBILE:
            return "PermanentAndMobile"