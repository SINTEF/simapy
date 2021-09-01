# Generated with RandomGenerator
# 
from enum import Enum
from enum import auto

class RandomGenerator(Enum):
    """"""
    LEGACY = auto()
    MERSENNE = auto()

    def label(self):
        if self == RandomGenerator.LEGACY:
            return "Legacy"
        if self == RandomGenerator.MERSENNE:
            return "Mersenne twister"