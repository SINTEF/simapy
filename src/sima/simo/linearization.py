# Generated with Linearization
# 
from enum import Enum
from enum import auto

class Linearization(Enum):
    """"""
    STOCHASTIC = auto()
    DIFFERENTIATION = auto()

    def label(self):
        if self == Linearization.STOCHASTIC:
            return "Stochastic"
        if self == Linearization.DIFFERENTIATION:
            return "Differentiation"