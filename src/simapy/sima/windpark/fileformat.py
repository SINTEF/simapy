# Generated with FileFormat
# 
from enum import Enum
from enum import auto

class FileFormat(Enum):
    """"""
    BINARY = auto()
    ASCII = auto()

    def label(self):
        if self == FileFormat.BINARY:
            return "Binary format"
        if self == FileFormat.ASCII:
            return "Ascii format"