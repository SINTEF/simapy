# Generated with BallastTankState
# 
from enum import Enum
from enum import auto

class BallastTankState(Enum):
    """"""
    INTACT = auto()
    DAMAGED = auto()

    def label(self):
        if self == BallastTankState.INTACT:
            return "Intact"
        if self == BallastTankState.DAMAGED:
            return "Damaged"