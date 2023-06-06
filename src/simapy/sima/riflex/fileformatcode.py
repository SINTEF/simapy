# Generated with FileFormatCode
# 
from enum import Enum
from enum import auto

class FileFormatCode(Enum):
    """"""
    BINARY_OUTPUT_ONLY = auto()
    ASCII_OUTPUT_ONLY = auto()
    NO_ADDITIONAL_OUTPUT = auto()
    ASCII_OUTPUT = auto()
    BINARY_OUTPUT = auto()

    def label(self):
        if self == FileFormatCode.BINARY_OUTPUT_ONLY:
            return "Binary format"
        if self == FileFormatCode.ASCII_OUTPUT_ONLY:
            return "ASCII format"
        if self == FileFormatCode.NO_ADDITIONAL_OUTPUT:
            return "Outmod (IFNDYN) format"
        if self == FileFormatCode.ASCII_OUTPUT:
            return "Outmod (IFNDYN) and ASCII format"
        if self == FileFormatCode.BINARY_OUTPUT:
            return "Outmod (IFNDYN) and Binary format"