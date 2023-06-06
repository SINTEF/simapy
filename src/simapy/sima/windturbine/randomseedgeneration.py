# Generated with RandomSeedGeneration
# 
from enum import Enum
from enum import auto

class RandomSeedGeneration(Enum):
    """"""
    INTRINSIC = auto()
    RANLUX = auto()
    RNSNLW = auto()

    def label(self):
        if self == RandomSeedGeneration.INTRINSIC:
            return "Intrinsic"
        if self == RandomSeedGeneration.RANLUX:
            return "RanLux"
        if self == RandomSeedGeneration.RNSNLW:
            return "RNSNLW"