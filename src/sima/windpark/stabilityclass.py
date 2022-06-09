# Generated with StabilityClass
# 
from enum import Enum
from enum import auto

class StabilityClass(Enum):
    """"""
    STABLE_0 = auto()
    STABLE_1 = auto()
    STABLE_2 = auto()
    STABLE_3 = auto()
    STABLE_4 = auto()
    STABLE_5 = auto()
    STABLE_6 = auto()
    STABLE_7 = auto()

    def label(self):
        if self == StabilityClass.STABLE_0:
            return "None"
        if self == StabilityClass.STABLE_1:
            return "Very stable stability class: Monin-Obukhov length scale (10 < L < 50)"
        if self == StabilityClass.STABLE_2:
            return "Stable stability class: Monin-Obukhov length scale (50 < L < 200)"
        if self == StabilityClass.STABLE_3:
            return "Near stable stability class: Monin-Obukhov length scale (200 < L < 500)"
        if self == StabilityClass.STABLE_4:
            return "Neutral stability class: Monin-Obukhov length scale (abs(L) > 500)"
        if self == StabilityClass.STABLE_5:
            return "Near unstable stability class: Monin-Obukhov length scale (-500 < L < -200)"
        if self == StabilityClass.STABLE_6:
            return "Unstable stability class: Monin-Obukhov length scale (-200 <L < -100)"
        if self == StabilityClass.STABLE_7:
            return "Very unstable stability class: Monin-Obukhov length scale (-100 <L < -50)"