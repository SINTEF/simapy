# Generated with HydroSystemFilterMethod
# 
from enum import Enum
from enum import auto

class HydroSystemFilterMethod(Enum):
    """"""
    BLOCKED = auto()
    NONE = auto()
    ACTIVE = auto()

    def label(self):
        if self == HydroSystemFilterMethod.BLOCKED:
            return "Block low pass translation velocities."
        if self == HydroSystemFilterMethod.NONE:
            return "No filtering"
        if self == HydroSystemFilterMethod.ACTIVE:
            return "Filter activated"