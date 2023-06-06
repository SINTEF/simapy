# Generated with TorsionStiffness
# 
from enum import Enum
from enum import auto

class TorsionStiffness(Enum):
    """"""
    CONSTANT = auto()
    UNSYMMETRIC = auto()
    SYMMETRIC = auto()
    GENERAL_TORSION_RELATION = auto()

    def label(self):
        if self == TorsionStiffness.CONSTANT:
            return "Constant"
        if self == TorsionStiffness.UNSYMMETRIC:
            return "Unsymmetric"
        if self == TorsionStiffness.SYMMETRIC:
            return "Symmetric"
        if self == TorsionStiffness.GENERAL_TORSION_RELATION:
            return "General torsion / relation"