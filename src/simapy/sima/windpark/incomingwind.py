# Generated with IncomingWind
# 
from enum import Enum
from enum import auto

class IncomingWind(Enum):
    """"""
    AMBIENT = auto()
    INCOMING = auto()

    def label(self):
        if self == IncomingWind.AMBIENT:
            return "Ambient"
        if self == IncomingWind.INCOMING:
            return "Incoming"