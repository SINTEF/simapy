# Generated with Severity
# 
from enum import Enum
from enum import auto

class Severity(Enum):
    """"""
    WARNING = auto()
    ERROR = auto()
    INFO = auto()
    COMMENT = auto()

    def label(self):
        if self == Severity.WARNING:
            return "Warning"
        if self == Severity.ERROR:
            return "Error"
        if self == Severity.INFO:
            return "Info"
        if self == Severity.COMMENT:
            return "Comment"