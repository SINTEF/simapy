# Generated with ConstraintType
# 
from enum import Enum
from enum import auto

class ConstraintType(Enum):
    """"""
    LE = auto()
    LT = auto()
    GE = auto()
    GT = auto()

    def label(self):
        if self == ConstraintType.LE:
            return "<="
        if self == ConstraintType.LT:
            return "<"
        if self == ConstraintType.GE:
            return ">="
        if self == ConstraintType.GT:
            return ">"