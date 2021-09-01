# Generated with FileFormat
# 
from enum import Enum
from enum import auto

class FileFormat(Enum):
    """"""
    CSV = auto()
    COLUMN = auto()
    HDF5 = auto()
    EXCEL = auto()
    JSON = auto()
    AUTOMATIC = auto()

    def label(self):
        if self == FileFormat.CSV:
            return "CSV"
        if self == FileFormat.COLUMN:
            return "Column"
        if self == FileFormat.HDF5:
            return "HDF5"
        if self == FileFormat.EXCEL:
            return "Excel"
        if self == FileFormat.JSON:
            return "Json"
        if self == FileFormat.AUTOMATIC:
            return "Automatic"