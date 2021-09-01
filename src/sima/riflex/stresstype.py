# Generated with StressType
# 
from enum import Enum
from enum import auto

class StressType(Enum):
    """"""
    AXIAL_BENDING = auto()
    TRUE_WALL = auto()
    AXIAL_STRESS = auto()
    VON_MISES = auto()

    def label(self):
        if self == StressType.AXIAL_BENDING:
            return "Axial bending stress"
        if self == StressType.TRUE_WALL:
            return "True wall axial stress"
        if self == StressType.AXIAL_STRESS:
            return "Resultant axial stress"
        if self == StressType.VON_MISES:
            return "Von mises stress"