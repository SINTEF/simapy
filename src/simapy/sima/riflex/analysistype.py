# Generated with AnalysisType
# 
from enum import Enum
from enum import auto

class AnalysisType(Enum):
    """"""
    IRREGULAR = auto()
    REGULAR = auto()

    def label(self):
        if self == AnalysisType.IRREGULAR:
            return "Irregular waves"
        if self == AnalysisType.REGULAR:
            return "Regular wave / motion"