# Generated with MeanderingAnalysisOption
# 
from enum import Enum
from enum import auto

class MeanderingAnalysisOption(Enum):
    """"""
    COMP = auto()
    SKIP = auto()

    def label(self):
        if self == MeanderingAnalysisOption.COMP:
            return "Compute"
        if self == MeanderingAnalysisOption.SKIP:
            return "Skip"