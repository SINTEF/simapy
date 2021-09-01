# Generated with LinearSystemSolvingMethod
# 
from enum import Enum
from enum import auto

class LinearSystemSolvingMethod(Enum):
    """"""
    ITERATIVE = auto()
    DIRECT = auto()
    BLOCKITERATIVE = auto()

    def label(self):
        if self == LinearSystemSolvingMethod.ITERATIVE:
            return "Iterative"
        if self == LinearSystemSolvingMethod.DIRECT:
            return "Direct"
        if self == LinearSystemSolvingMethod.BLOCKITERATIVE:
            return "Block iterative"