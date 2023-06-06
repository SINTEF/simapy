# Generated with GeometryOrderOption
# 
from enum import Enum
from enum import auto

class GeometryOrderOption(Enum):
    """"""
    LOW = auto()
    HIGH = auto()

    def label(self):
        if self == GeometryOrderOption.LOW:
            return "Low"
        if self == GeometryOrderOption.HIGH:
            return "High"