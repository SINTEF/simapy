# Generated with CoordinateSystem
# 
from enum import Enum
from enum import auto

class CoordinateSystem(Enum):
    """"""
    LOCAL = auto()
    GLOBAL = auto()

    def label(self):
        if self == CoordinateSystem.LOCAL:
            return "Local"
        if self == CoordinateSystem.GLOBAL:
            return "Global"