# Generated with CalculateExcitingForcesOption
# 
from enum import Enum
from enum import auto

class CalculateExcitingForcesOption(Enum):
    """"""
    NO = auto()
    YES = auto()
    YESSEPARATE = auto()

    def label(self):
        if self == CalculateExcitingForcesOption.NO:
            return "No"
        if self == CalculateExcitingForcesOption.YES:
            return "Yes"
        if self == CalculateExcitingForcesOption.YESSEPARATE:
            return "Yes - separate"