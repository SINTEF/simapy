# Generated with NumberFormat
# 
from enum import Enum
from enum import auto

class NumberFormat(Enum):
    """"""
    AUTOFORMAT = auto()
    GENERAL = auto()
    SCIENTIFIC = auto()

    def label(self):
        if self == NumberFormat.AUTOFORMAT:
            return "Autoformat"
        if self == NumberFormat.GENERAL:
            return "General"
        if self == NumberFormat.SCIENTIFIC:
            return "Scientific"