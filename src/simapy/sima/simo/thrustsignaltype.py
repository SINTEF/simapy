# Generated with ThrustSignalType
# 
from enum import Enum
from enum import auto

class ThrustSignalType(Enum):
    """"""
    FORCE = auto()
    RPS = auto()

    def label(self):
        if self == ThrustSignalType.FORCE:
            return "Force"
        if self == ThrustSignalType.RPS:
            return "Rotations per second"