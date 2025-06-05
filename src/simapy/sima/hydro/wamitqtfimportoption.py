# Generated with WamitQtfImportOption
# 
from enum import Enum
from enum import auto

class WamitQtfImportOption(Enum):
    """"""
    NONE = auto()
    DIRECT = auto()
    INDIRECT = auto()

    def label(self):
        if self == WamitQtfImportOption.NONE:
            return "None"
        if self == WamitQtfImportOption.DIRECT:
            return "Direct"
        if self == WamitQtfImportOption.INDIRECT:
            return "Indirect"