# Generated with BodyForceReferenceSystem
# 
from enum import Enum
from enum import auto

class BodyForceReferenceSystem(Enum):
    """"""
    BODY_LOCAL = auto()
    GLOBAL = auto()

    def label(self):
        if self == BodyForceReferenceSystem.BODY_LOCAL:
            return "Body Local"
        if self == BodyForceReferenceSystem.GLOBAL:
            return "Global"