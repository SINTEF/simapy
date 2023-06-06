# Generated with YawControllerType
# 
from enum import Enum
from enum import auto

class YawControllerType(Enum):
    """"""
    NONE = auto()
    INTERNAL = auto()
    COMBINED = auto()

    def label(self):
        if self == YawControllerType.NONE:
            return "No yaw controller"
        if self == YawControllerType.INTERNAL:
            return "Internal controller"
        if self == YawControllerType.COMBINED:
            return "Combined external controller"