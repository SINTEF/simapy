# Generated with FrequencyAnalysisType
# 
from enum import Enum
from enum import auto

class FrequencyAnalysisType(Enum):
    """"""
    WAVE_FREQUENCY = auto()
    LOW_FREQUENCY = auto()
    LOW_AND_WAVE_FREQUENCY = auto()

    def label(self):
        if self == FrequencyAnalysisType.WAVE_FREQUENCY:
            return "Wave frequency"
        if self == FrequencyAnalysisType.LOW_FREQUENCY:
            return "Low frequency"
        if self == FrequencyAnalysisType.LOW_AND_WAVE_FREQUENCY:
            return "Low and wave frequency"