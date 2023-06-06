# Generated with FailureMode
# 
from enum import Enum
from enum import auto

class FailureMode(Enum):
    """"""
    NONE = auto()
    FAIL = auto()

    def label(self):
        if self == FailureMode.NONE:
            return "None"
        if self == FailureMode.FAIL:
            return "Fail"