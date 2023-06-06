# Generated with Plane
# 
from enum import Enum
from enum import auto

class Plane(Enum):
    """"""
    XY = auto()
    XZ = auto()
    YZ = auto()

    def label(self):
        if self == Plane.XY:
            return "XY"
        if self == Plane.XZ:
            return "XZ"
        if self == Plane.YZ:
            return "YZ"