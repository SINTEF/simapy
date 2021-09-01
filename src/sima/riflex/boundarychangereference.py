# Generated with BoundaryChangeReference
# 
from enum import Enum
from enum import auto

class BoundaryChangeReference(Enum):
    """"""
    SUPERNODE = auto()
    NODE = auto()

    def label(self):
        if self == BoundaryChangeReference.SUPERNODE:
            return "Supernode"
        if self == BoundaryChangeReference.NODE:
            return "Node"