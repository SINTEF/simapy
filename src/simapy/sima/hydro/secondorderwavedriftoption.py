# Generated with SecondOrderWaveDriftOption
# 
from enum import Enum
from enum import auto

class SecondOrderWaveDriftOption(Enum):
    """"""
    COMBINED = auto()
    MEAN = auto()
    HORIZONTAL = auto()

    def label(self):
        if self == SecondOrderWaveDriftOption.COMBINED:
            return "COMBINED"
        if self == SecondOrderWaveDriftOption.MEAN:
            return "MEAN"
        if self == SecondOrderWaveDriftOption.HORIZONTAL:
            return "HORIZONTAL"