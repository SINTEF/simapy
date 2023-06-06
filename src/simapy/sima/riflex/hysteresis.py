# Generated with Hysteresis
# 
from enum import Enum
from enum import auto

class Hysteresis(Enum):
    """"""
    NO_HYSTERESIS = auto()
    GENERATED_HYSTERESIS = auto()

    def label(self):
        if self == Hysteresis.NO_HYSTERESIS:
            return "No hysteresis"
        if self == Hysteresis.GENERATED_HYSTERESIS:
            return "Generated hysteresis"