# Generated with GeotechnicalPileType
# 
from enum import Enum
from enum import auto

class GeotechnicalPileType(Enum):
    """"""
    OPEN = auto()
    CLOSED = auto()

    def label(self):
        if self == GeotechnicalPileType.OPEN:
            return "Open-ended"
        if self == GeotechnicalPileType.CLOSED:
            return "Closed"