# Generated with RandomGenerator
# 
from enum import Enum
from enum import auto

class RandomGenerator(Enum):
    """"""
    MERSENNE = auto()
    LEGACY = auto()

    def label(self):
        if self == RandomGenerator.MERSENNE:
            return "Mersenne twister"
        if self == RandomGenerator.LEGACY:
            return "Legacy"