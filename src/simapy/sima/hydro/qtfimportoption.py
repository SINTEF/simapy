# Generated with QTFImportOption
# 
from enum import Enum
from enum import auto

class QTFImportOption(Enum):
    """"""
    ANY = auto()
    DIFF = auto()
    SUM = auto()
    NONE = auto()

    def label(self):
        if self == QTFImportOption.ANY:
            return "ANY"
        if self == QTFImportOption.DIFF:
            return "DIFF"
        if self == QTFImportOption.SUM:
            return "SUM"
        if self == QTFImportOption.NONE:
            return "NONE"