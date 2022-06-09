# Generated with LowPassFrequencyOption
# 
from enum import Enum
from enum import auto

class LowPassFrequencyOption(Enum):
    """"""
    CALC = auto()
    SPEC = auto()

    def label(self):
        if self == LowPassFrequencyOption.CALC:
            return "Calculate"
        if self == LowPassFrequencyOption.SPEC:
            return "Specify"