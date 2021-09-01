# Generated with ControlDOF
# 
from enum import Enum
from enum import auto

class ControlDOF(Enum):
    """"""
    NONE = auto()
    SURGE = auto()
    SWAY = auto()
    HEAVE = auto()
    ROLL = auto()
    PITCH = auto()
    YAW = auto()

    def label(self):
        if self == ControlDOF.NONE:
            return "None"
        if self == ControlDOF.SURGE:
            return "Surge"
        if self == ControlDOF.SWAY:
            return "Sway"
        if self == ControlDOF.HEAVE:
            return "Heave"
        if self == ControlDOF.ROLL:
            return "Roll"
        if self == ControlDOF.PITCH:
            return "Pitch"
        if self == ControlDOF.YAW:
            return "Yaw"