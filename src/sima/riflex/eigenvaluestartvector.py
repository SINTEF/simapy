# Generated with EigenvalueStartVector
# 
from enum import Enum
from enum import auto

class EigenvalueStartVector(Enum):
    """"""
    PSEUDORANDOM_STARTVECTOR = auto()
    DIAGONAL_OF_MASS_MATRIX = auto()
    STARTVECTOR = auto()

    def label(self):
        if self == EigenvalueStartVector.PSEUDORANDOM_STARTVECTOR:
            return "Generated pseudo random start vector"
        if self == EigenvalueStartVector.DIAGONAL_OF_MASS_MATRIX:
            return "Use diagonal of mass matrix"
        if self == EigenvalueStartVector.STARTVECTOR:
            return "Use start vector of unit elements"