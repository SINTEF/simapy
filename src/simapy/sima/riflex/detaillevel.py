# Generated with DetailLevel
# 
from enum import Enum
from enum import auto

class DetailLevel(Enum):
    """"""
    MINIMUM = auto()
    MEDIUM = auto()
    MAXIMUM = auto()

    def label(self):
        if self == DetailLevel.MINIMUM:
            return "Minimum"
        if self == DetailLevel.MEDIUM:
            return "Medium"
        if self == DetailLevel.MAXIMUM:
            return "Maximum"