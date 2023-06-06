# Generated with RotationalStiffnessType
# 
from enum import Enum
from enum import auto

class RotationalStiffnessType(Enum):
    """"""
    FIXED = auto()
    FREE = auto()
    LINEAR = auto()
    NON_LINEAR = auto()

    def label(self):
        if self == RotationalStiffnessType.FIXED:
            return "Fixed"
        if self == RotationalStiffnessType.FREE:
            return "Free"
        if self == RotationalStiffnessType.LINEAR:
            return "Linear"
        if self == RotationalStiffnessType.NON_LINEAR:
            return "Non linear"