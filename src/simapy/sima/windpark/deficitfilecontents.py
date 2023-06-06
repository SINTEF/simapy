# Generated with DeficitFileContents
# 
from enum import Enum
from enum import auto

class DeficitFileContents(Enum):
    """"""
    INDUCTION_PROFILE = auto()
    START_DEFICIT = auto()

    def label(self):
        if self == DeficitFileContents.INDUCTION_PROFILE:
            return "Induction profile"
        if self == DeficitFileContents.START_DEFICIT:
            return "Start deficit"