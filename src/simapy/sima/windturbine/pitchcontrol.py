# Generated with PitchControl
# 
from enum import Enum
from enum import auto

class PitchControl(Enum):
    """"""
    COLLECTIVE = auto()
    INDIVIDUAL = auto()

    def label(self):
        if self == PitchControl.COLLECTIVE:
            return "Collective"
        if self == PitchControl.INDIVIDUAL:
            return "Individual"