# Generated with WallPoint
# 
from enum import Enum
from enum import auto

class WallPoint(Enum):
    """"""
    OUTER_WALL = auto()
    INNER_WALL = auto()

    def label(self):
        if self == WallPoint.OUTER_WALL:
            return "Outer wall"
        if self == WallPoint.INNER_WALL:
            return "Inner wall"