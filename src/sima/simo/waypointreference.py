# Generated with WaypointReference
# 
from enum import Enum
from enum import auto

class WaypointReference(Enum):
    """"""
    LOCAL = auto()
    GLOBAL = auto()

    def label(self):
        if self == WaypointReference.LOCAL:
            return "Locally defined relative to body location"
        if self == WaypointReference.GLOBAL:
            return "Globally defined"