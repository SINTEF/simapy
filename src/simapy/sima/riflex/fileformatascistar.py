# Generated with FileFormatAsciStar
# 
from enum import Enum
from enum import auto

class FileFormatAsciStar(Enum):
    """"""
    ASCII = auto()
    STARTIMES = auto()

    def label(self):
        if self == FileFormatAsciStar.ASCII:
            return "ASCII"
        if self == FileFormatAsciStar.STARTIMES:
            return "STARTIMES"