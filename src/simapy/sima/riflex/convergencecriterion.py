# Generated with ConvergenceCriterion
# 
from enum import Enum
from enum import auto

class ConvergenceCriterion(Enum):
    """"""
    AMPNOR = auto()
    DIFMAX = auto()
    NONE = auto()

    def label(self):
        if self == ConvergenceCriterion.AMPNOR:
            return "AMPNOR"
        if self == ConvergenceCriterion.DIFMAX:
            return "DIFMAX"
        if self == ConvergenceCriterion.NONE:
            return "NONE"