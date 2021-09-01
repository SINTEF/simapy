# Generated with CalculateMeanForceAndMomentIntegrationOption
# 
from enum import Enum
from enum import auto

class CalculateMeanForceAndMomentIntegrationOption(Enum):
    """"""
    NO = auto()
    YESUNIDIRECTIONAL = auto()
    YESFORALL = auto()

    def label(self):
        if self == CalculateMeanForceAndMomentIntegrationOption.NO:
            return "No"
        if self == CalculateMeanForceAndMomentIntegrationOption.YESUNIDIRECTIONAL:
            return "Yes - unidirectional"
        if self == CalculateMeanForceAndMomentIntegrationOption.YESFORALL:
            return "Yes - for all"