# Generated with IncomingWind
# 
from enum import Enum
from enum import auto

class IncomingWind(Enum):
    """"""
    CONSTANT = auto()
    INCOMING = auto()

    def label(self):
        if self == IncomingWind.CONSTANT:
            return "Constant"
        if self == IncomingWind.INCOMING:
            return "Incoming"