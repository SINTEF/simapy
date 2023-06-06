# Generated with ResponseFrequencyOption
# 
from enum import Enum
from enum import auto

class ResponseFrequencyOption(Enum):
    """"""
    CONCURRENT = auto()
    CONSECUTIVE = auto()

    def label(self):
        if self == ResponseFrequencyOption.CONCURRENT:
            return "Concurrent"
        if self == ResponseFrequencyOption.CONSECUTIVE:
            return "Consecutive"