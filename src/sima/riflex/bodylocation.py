# Generated with BodyLocation
# 
from enum import Enum
from enum import auto

class BodyLocation(Enum):
    """"""
    ELEMENT = auto()
    NODE = auto()
    SUPER_NODE = auto()
    POSITION = auto()

    def label(self):
        if self == BodyLocation.ELEMENT:
            return "Element"
        if self == BodyLocation.NODE:
            return "Node"
        if self == BodyLocation.SUPER_NODE:
            return "Supernode"
        if self == BodyLocation.POSITION:
            return "Position"