# Generated with ThrustCoefficientModel
# 
from enum import Enum
from enum import auto

class ThrustCoefficientModel(Enum):
    """"""
    INTERNAL = auto()
    FORWARD = auto()
    SEPARATE = auto()

    def label(self):
        if self == ThrustCoefficientModel.INTERNAL:
            return "Internal"
        if self == ThrustCoefficientModel.FORWARD:
            return "Forward"
        if self == ThrustCoefficientModel.SEPARATE:
            return "Separate"