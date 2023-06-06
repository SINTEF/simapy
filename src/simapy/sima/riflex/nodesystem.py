# Generated with NodeSystem
# 
from enum import Enum
from enum import auto

class NodeSystem(Enum):
    """"""
    GLOBAL = auto()
    SHAFT0 = auto()

    def label(self):
        if self == NodeSystem.GLOBAL:
            return "Global"
        if self == NodeSystem.SHAFT0:
            return "Shaft"