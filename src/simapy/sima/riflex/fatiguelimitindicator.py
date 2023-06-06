# Generated with FatigueLimitIndicator
# 
from enum import Enum
from enum import auto

class FatigueLimitIndicator(Enum):
    """"""
    NO_LIMIT = auto()
    STRESS_CYCLES = auto()
    STRESS_RANGE = auto()

    def label(self):
        if self == FatigueLimitIndicator.NO_LIMIT:
            return "No fatigue limit"
        if self == FatigueLimitIndicator.STRESS_CYCLES:
            return "Stress cycles"
        if self == FatigueLimitIndicator.STRESS_RANGE:
            return "Stress range"