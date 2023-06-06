# Generated with AmplitudeType
# 
from enum import Enum
from enum import auto

class AmplitudeType(Enum):
    """"""
    SINGLE = auto()
    DOUBLE = auto()

    def label(self):
        if self == AmplitudeType.SINGLE:
            return "Single"
        if self == AmplitudeType.DOUBLE:
            return "Double"