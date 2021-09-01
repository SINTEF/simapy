# Generated with StressJointLoadFormulation
# 
from enum import Enum
from enum import auto

class StressJointLoadFormulation(Enum):
    """"""
    MORISON = auto()
    TVIV = auto()
    NONE = auto()

    def label(self):
        if self == StressJointLoadFormulation.MORISON:
            return "Morison"
        if self == StressJointLoadFormulation.TVIV:
            return "Time domain VIV"
        if self == StressJointLoadFormulation.NONE:
            return "None"