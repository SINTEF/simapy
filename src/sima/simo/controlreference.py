# Generated with ControlReference
# 
from enum import Enum
from enum import auto

class ControlReference(Enum):
    """"""
    GLOBAL = auto()
    BODY = auto()
    WAYPOINT = auto()
    GBCIRCLE = auto()

    def label(self):
        if self == ControlReference.GLOBAL:
            return "Global"
        if self == ControlReference.BODY:
            return "Body Relative"
        if self == ControlReference.WAYPOINT:
            return "Waypoint"
        if self == ControlReference.GBCIRCLE:
            return "Global circle"