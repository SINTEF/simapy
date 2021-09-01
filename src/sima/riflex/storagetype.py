# Generated with StorageType
# 
from enum import Enum
from enum import auto

class StorageType(Enum):
    """"""
    BINARY = auto()
    ASCII = auto()

    def label(self):
        if self == StorageType.BINARY:
            return "Binary format"
        if self == StorageType.ASCII:
            return "ASCII format"