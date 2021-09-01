# Generated with SlugForceInterruption
# 
from enum import Enum
from enum import auto

class SlugForceInterruption(Enum):
    """"""
    SLUG = auto()
    SIMULATION_LENGTH = auto()

    def label(self):
        if self == SlugForceInterruption.SLUG:
            return "Analysis termination controlled by slug"
        if self == SlugForceInterruption.SIMULATION_LENGTH:
            return "Analysis termination controlled by specified length of simulation"