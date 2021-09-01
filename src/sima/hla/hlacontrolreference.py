# Generated with HLAControlReference
# 
from enum import Enum
from enum import auto

class HLAControlReference(Enum):
    """"""
    POSITION = auto()
    VELOCITY = auto()
    FORCE = auto()

    def label(self):
        if self == HLAControlReference.POSITION:
            return "Position"
        if self == HLAControlReference.VELOCITY:
            return "Velocity"
        if self == HLAControlReference.FORCE:
            return "Force"