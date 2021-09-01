# Generated with EquilibriumCalculationOption
# 
from enum import Enum
from enum import auto

class EquilibriumCalculationOption(Enum):
    """"""
    TRANSIENT = auto()
    NEWTON_RAPHSON = auto()

    def label(self):
        if self == EquilibriumCalculationOption.TRANSIENT:
            return "Transient"
        if self == EquilibriumCalculationOption.NEWTON_RAPHSON:
            return "Newton-Raphson"