# Generated with IterationContinuationCode
# 
from enum import Enum
from enum import auto

class IterationContinuationCode(Enum):
    """"""
    CONTINUED = auto()
    INTERRUPTED = auto()

    def label(self):
        if self == IterationContinuationCode.CONTINUED:
            return "Continued"
        if self == IterationContinuationCode.INTERRUPTED:
            return "Interrupted"