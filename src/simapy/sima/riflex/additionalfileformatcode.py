# Generated with AdditionalFileFormatCode
# 
from enum import Enum
from enum import auto

class AdditionalFileFormatCode(Enum):
    """"""
    DEFAULT = auto()
    BINARY_OUTPUT = auto()
    ASCII_OUTPUT = auto()

    def label(self):
        if self == AdditionalFileFormatCode.DEFAULT:
            return "Default"
        if self == AdditionalFileFormatCode.BINARY_OUTPUT:
            return "Binary format"
        if self == AdditionalFileFormatCode.ASCII_OUTPUT:
            return "ASCII format"