# Generated with LoadAndMassFormulation
# 
from enum import Enum
from enum import auto

class LoadAndMassFormulation(Enum):
    """"""
    LUMPED = auto()
    CONSISTENT = auto()

    def label(self):
        if self == LoadAndMassFormulation.LUMPED:
            return "Lumped load and mass formulation"
        if self == LoadAndMassFormulation.CONSISTENT:
            return "Consistent load and mass formulation"