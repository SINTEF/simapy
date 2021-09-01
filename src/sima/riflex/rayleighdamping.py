# Generated with RayleighDamping
# 
from enum import Enum
from enum import auto

class RayleighDamping(Enum):
    """"""
    TOTAL = auto()
    MATERIAL = auto()

    def label(self):
        if self == RayleighDamping.TOTAL:
            return "Total stiffness damping"
        if self == RayleighDamping.MATERIAL:
            return "Material stiffness damping"