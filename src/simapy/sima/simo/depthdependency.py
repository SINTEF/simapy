# Generated with DepthDependency
# 
from enum import Enum
from enum import auto

class DepthDependency(Enum):
    """"""
    WAVE_ELEVATION = auto()
    WATER_PLANE = auto()

    def label(self):
        if self == DepthDependency.WAVE_ELEVATION:
            return "Wave elevation"
        if self == DepthDependency.WATER_PLANE:
            return "Water plane"