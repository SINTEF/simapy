# Generated with BendingStiffness
# 
from enum import Enum
from enum import auto

class BendingStiffness(Enum):
    """"""
    CONSTANT = auto()
    MOMENT_CURVATURE = auto()

    def label(self):
        if self == BendingStiffness.CONSTANT:
            return "Constant"
        if self == BendingStiffness.MOMENT_CURVATURE:
            return "Moment-curvature"