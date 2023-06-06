# Generated with ThrusterFailureMode
# 
from enum import Enum
from enum import auto

class ThrusterFailureMode(Enum):
    """"""
    NO_FAILURE = auto()
    THRUSTER_BLACKOUT = auto()

    def label(self):
        if self == ThrusterFailureMode.NO_FAILURE:
            return "No failure"
        if self == ThrusterFailureMode.THRUSTER_BLACKOUT:
            return "Thruster blackout"