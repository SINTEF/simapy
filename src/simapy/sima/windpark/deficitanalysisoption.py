# Generated with DeficitAnalysisOption
# 
from enum import Enum
from enum import auto

class DeficitAnalysisOption(Enum):
    """"""
    COMP = auto()
    READ = auto()

    def label(self):
        if self == DeficitAnalysisOption.COMP:
            return "Compute"
        if self == DeficitAnalysisOption.READ:
            return "Read"