# Generated with StabilityClass
# 
from enum import Enum
from enum import auto

class StabilityClass(Enum):
    """"""
    NONE = auto()
    VERY_STABLE = auto()
    STABLE = auto()
    NEAR_STABLE = auto()
    NEUTRAL = auto()
    NEAR_UNSTABLE = auto()
    UNSTABLE = auto()
    VERY_UNSTABLE = auto()

    def label(self):
        if self == StabilityClass.NONE:
            return "None"
        if self == StabilityClass.VERY_STABLE:
            return "Very stable"
        if self == StabilityClass.STABLE:
            return "Stable"
        if self == StabilityClass.NEAR_STABLE:
            return "Near stable"
        if self == StabilityClass.NEUTRAL:
            return "Neutral"
        if self == StabilityClass.NEAR_UNSTABLE:
            return "Near unstable"
        if self == StabilityClass.UNSTABLE:
            return "Unstable"
        if self == StabilityClass.VERY_UNSTABLE:
            return "Very unstable"