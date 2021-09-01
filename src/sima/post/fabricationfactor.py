# Generated with FabricationFactor
# 
from enum import Enum
from enum import auto

class FabricationFactor(Enum):
    """"""
    SEAMLESSPIPE = auto()
    UOEPIPE = auto()
    UOTRBPIPE = auto()

    def label(self):
        if self == FabricationFactor.SEAMLESSPIPE:
            return "Seamless Pipe (1.0)"
        if self == FabricationFactor.UOEPIPE:
            return "UOE Pipe (0.85)"
        if self == FabricationFactor.UOTRBPIPE:
            return "UOTRB Pipe (0.925)"