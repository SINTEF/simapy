# Generated with BoundaryCondition
# 
from enum import Enum
from enum import auto

class BoundaryCondition(Enum):
    """"""
    FREE = auto()
    FIXED = auto()

    def label(self):
        if self == BoundaryCondition.FREE:
            return "Free"
        if self == BoundaryCondition.FIXED:
            return "Fixed"