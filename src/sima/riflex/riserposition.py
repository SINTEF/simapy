# Generated with RiserPosition
# 
from enum import Enum
from enum import auto

class RiserPosition(Enum):
    """"""
    DYNAMIC_POSITIONS = auto()
    RISER_KEPT_FIXED = auto()
    STATIC_RISER_POSITION = auto()

    def label(self):
        if self == RiserPosition.DYNAMIC_POSITIONS:
            return "Dynamic positions"
        if self == RiserPosition.RISER_KEPT_FIXED:
            return "Riser kept fixed"
        if self == RiserPosition.STATIC_RISER_POSITION:
            return "Static riser position"