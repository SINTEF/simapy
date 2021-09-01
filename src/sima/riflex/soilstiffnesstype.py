# Generated with SoilStiffnessType
# 
from enum import Enum
from enum import auto

class SoilStiffnessType(Enum):
    """"""
    STATIC = auto()
    CYCLIC = auto()

    def label(self):
        if self == SoilStiffnessType.STATIC:
            return "Static"
        if self == SoilStiffnessType.CYCLIC:
            return "Cyclic"