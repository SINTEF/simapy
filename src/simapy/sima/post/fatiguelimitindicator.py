# Generated with FatigueLimitIndicator
# 
from enum import Enum
from enum import auto

class FatigueLimitIndicator(Enum):
    """"""
    STRESS_RANGE = auto()
    STRESS_CYCLES = auto()
    NO_LIMIT = auto()

    def label(self):
        if self == FatigueLimitIndicator.STRESS_RANGE:
            return "Stress range"
        if self == FatigueLimitIndicator.STRESS_CYCLES:
            return "Stress cycles"
        if self == FatigueLimitIndicator.NO_LIMIT:
            return "No limit"