# Generated with LoadType
# 
from enum import Enum
from enum import auto

class LoadType(Enum):
    """"""
    GRAVITY_AND_BUOYANCY_INCLUDED = auto()
    GRAVITY_AND_BUOYANCY_NOT_INCLUDED = auto()

    def label(self):
        if self == LoadType.GRAVITY_AND_BUOYANCY_INCLUDED:
            return "Gravity and buoyancy included"
        if self == LoadType.GRAVITY_AND_BUOYANCY_NOT_INCLUDED:
            return "Gravity and buoyancy NOT included"