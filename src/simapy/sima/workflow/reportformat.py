# Generated with ReportFormat
# 
from enum import Enum
from enum import auto

class ReportFormat(Enum):
    """"""
    WORD = auto()
    FRAGMENT = auto()

    def label(self):
        if self == ReportFormat.WORD:
            return "Word"
        if self == ReportFormat.FRAGMENT:
            return "Report fragment"