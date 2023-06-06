# Generated with StiffnessType
# 
from enum import Enum
from enum import auto

class StiffnessType(Enum):
    """"""
    LINEAR = auto()
    NON_LINEAR = auto()

    def label(self):
        if self == StiffnessType.LINEAR:
            return "Linear"
        if self == StiffnessType.NON_LINEAR:
            return "Non linear"