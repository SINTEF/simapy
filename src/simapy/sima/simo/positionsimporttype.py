# Generated with PositionsImportType
# 
from enum import Enum
from enum import auto

class PositionsImportType(Enum):
    """"""
    FIXED_POSITION = auto()
    FROM_FILE = auto()
    ARTICULATED_STRUCTURE = auto()

    def label(self):
        if self == PositionsImportType.FIXED_POSITION:
            return "Fixed position"
        if self == PositionsImportType.FROM_FILE:
            return "Read from file"
        if self == PositionsImportType.ARTICULATED_STRUCTURE:
            return "Articulated structure"