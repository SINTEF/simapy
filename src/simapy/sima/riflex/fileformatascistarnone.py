# Generated with FileFormatAsciStarNone
# 
from enum import Enum
from enum import auto

class FileFormatAsciStarNone(Enum):
    """"""
    ASCII = auto()
    STARTIMES = auto()
    NONE = auto()

    def label(self):
        if self == FileFormatAsciStarNone.ASCII:
            return "ASCII"
        if self == FileFormatAsciStarNone.STARTIMES:
            return "STARTIMES"
        if self == FileFormatAsciStarNone.NONE:
            return "NONE"