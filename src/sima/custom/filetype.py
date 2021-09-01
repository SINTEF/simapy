# Generated with FileType
# 
from enum import Enum
from enum import auto

class FileType(Enum):
    """"""
    INPUT = auto()
    OUTPUT = auto()

    def label(self):
        if self == FileType.INPUT:
            return "Input"
        if self == FileType.OUTPUT:
            return "Output"