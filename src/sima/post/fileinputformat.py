# Generated with FileInputFormat
# 
from enum import Enum
from enum import auto

class FileInputFormat(Enum):
    """"""
    AUTOMATIC = auto()
    CSV = auto()

    def label(self):
        if self == FileInputFormat.AUTOMATIC:
            return "Automatic"
        if self == FileInputFormat.CSV:
            return "CSV"