# Generated with MassSummaryStep
# 
from enum import Enum
from enum import auto

class MassSummaryStep(Enum):
    """"""
    FINAL = auto()
    INITIAL = auto()

    def label(self):
        if self == MassSummaryStep.FINAL:
            return "FINAL"
        if self == MassSummaryStep.INITIAL:
            return "INITIAL"