# Generated with VonMisesStress
# 
from enum import Enum
from enum import auto

class VonMisesStress(Enum):
    """"""
    MIDWALL = auto()
    MAXIMUM = auto()

    def label(self):
        if self == VonMisesStress.MIDWALL:
            return "Mid wall"
        if self == VonMisesStress.MAXIMUM:
            return "Maximum"