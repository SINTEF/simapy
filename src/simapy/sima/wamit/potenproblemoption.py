# Generated with PotenProblemOption
# 
from enum import Enum
from enum import auto

class PotenProblemOption(Enum):
    """"""
    YESFORALL = auto()
    YESFORSPECIFIED = auto()
    NO = auto()

    def label(self):
        if self == PotenProblemOption.YESFORALL:
            return "Yes - for all modes"
        if self == PotenProblemOption.YESFORSPECIFIED:
            return "Yes - for specified modes"
        if self == PotenProblemOption.NO:
            return "No"