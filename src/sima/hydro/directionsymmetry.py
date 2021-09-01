# Generated with DirectionSymmetry
# 
from enum import Enum
from enum import auto

class DirectionSymmetry(Enum):
    """"""
    NO_SYMMETRY = auto()
    Y0_SYMMETRY = auto()
    DOUBLE_SYMMETRY = auto()
    X0_SYMMETRY = auto()

    def label(self):
        if self == DirectionSymmetry.NO_SYMMETRY:
            return "No symmetry"
        if self == DirectionSymmetry.Y0_SYMMETRY:
            return "Symmetry about Y=0"
        if self == DirectionSymmetry.DOUBLE_SYMMETRY:
            return "Double symmetry"
        if self == DirectionSymmetry.X0_SYMMETRY:
            return "Symmetry about X=0"