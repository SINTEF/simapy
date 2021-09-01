# Generated with ActivationFailureMode
# 
from enum import Enum
from enum import auto

class ActivationFailureMode(Enum):
    """"""
    NONE = auto()
    FAIL = auto()
    ACTIVATE = auto()

    def label(self):
        if self == ActivationFailureMode.NONE:
            return "None"
        if self == ActivationFailureMode.FAIL:
            return "Fail"
        if self == ActivationFailureMode.ACTIVATE:
            return "Activate"