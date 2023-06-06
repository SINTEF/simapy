# Generated with CalculateResponseAmplitudeOperatorOption
# 
from enum import Enum
from enum import auto

class CalculateResponseAmplitudeOperatorOption(Enum):
    """"""
    NO = auto()
    YESHASKIND = auto()
    YESDIFFRACTION = auto()

    def label(self):
        if self == CalculateResponseAmplitudeOperatorOption.NO:
            return "No"
        if self == CalculateResponseAmplitudeOperatorOption.YESHASKIND:
            return "Yes - Haskind"
        if self == CalculateResponseAmplitudeOperatorOption.YESDIFFRACTION:
            return "Yes - diffraction"