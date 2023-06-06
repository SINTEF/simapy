# Generated with WeightOption
# 
from enum import Enum
from enum import auto

class WeightOption(Enum):
    """"""
    UNIFORM = auto()
    TRUNCATED_JINC = auto()
    WINDOWED_JINC = auto()

    def label(self):
        if self == WeightOption.UNIFORM:
            return "Uniform"
        if self == WeightOption.TRUNCATED_JINC:
            return "Truncated Jinc"
        if self == WeightOption.WINDOWED_JINC:
            return "Window Jinc"