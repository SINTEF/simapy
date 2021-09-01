# Generated with EvaluationModeOption
# 
from enum import Enum
from enum import auto

class EvaluationModeOption(Enum):
    """"""
    FAST = auto()
    ACCURATE = auto()

    def label(self):
        if self == EvaluationModeOption.FAST:
            return "Fast"
        if self == EvaluationModeOption.ACCURATE:
            return "Accurate"