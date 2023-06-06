# Generated with ScalingOption
# 
from enum import Enum
from enum import auto

class ScalingOption(Enum):
    """"""
    NONE = auto()
    STANDARD = auto()
    POINT_SCALING = auto()
    GRID_POINT_SCALING = auto()

    def label(self):
        if self == ScalingOption.NONE:
            return "None"
        if self == ScalingOption.STANDARD:
            return "Standard scaling"
        if self == ScalingOption.POINT_SCALING:
            return "Point scaling"
        if self == ScalingOption.GRID_POINT_SCALING:
            return "Grid point scaling"