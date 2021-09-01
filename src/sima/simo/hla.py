# Generated with HLA
# 
from enum import Enum
from enum import auto

class HLA(Enum):
    """"""
    NO_IMPORT = auto()
    IMPORT = auto()

    def label(self):
        if self == HLA.NO_IMPORT:
            return "No import"
        if self == HLA.IMPORT:
            return "Import"