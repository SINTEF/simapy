# Generated with SurfaceType
# 
from enum import Enum
from enum import auto

class SurfaceType(Enum):
    """"""
    OCEAN_SURFACE = auto()
    SEA_FLOOR = auto()

    def label(self):
        if self == SurfaceType.OCEAN_SURFACE:
            return "Ocean surface"
        if self == SurfaceType.SEA_FLOOR:
            return "Seafloor"