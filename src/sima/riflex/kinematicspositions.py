# Generated with KinematicsPositions
# 
from enum import Enum
from enum import auto

class KinematicsPositions(Enum):
    """"""
    STATIC = auto()
    FIXED_STATIC = auto()
    DYNAMIC = auto()
    STATIC_CALCULATED = auto()

    def label(self):
        if self == KinematicsPositions.STATIC:
            return "Kinematics at static positions"
        if self == KinematicsPositions.FIXED_STATIC:
            return "Kinematics at fixed static position (linearized)"
        if self == KinematicsPositions.DYNAMIC:
            return "Kinematics at dynamic position calculated during simulation"
        if self == KinematicsPositions.STATIC_CALCULATED:
            return "Kinematics at static position calculated during simulation"