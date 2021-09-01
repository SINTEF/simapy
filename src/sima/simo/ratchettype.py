# Generated with RatchetType
# 
from enum import Enum
from enum import auto

class RatchetType(Enum):
    """"""
    TENSION = auto()
    COMPRESSION = auto()

    def label(self):
        if self == RatchetType.TENSION:
            return "Tension element"
        if self == RatchetType.COMPRESSION:
            return "Compression Element"