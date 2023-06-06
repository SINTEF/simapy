# Generated with ForceUnit
# 
from enum import Enum
from enum import auto

class ForceUnit(Enum):
    """"""
    NEWTON = auto()
    KILO_NEWTON = auto()
    MEGA_NEWTON = auto()
    TONNE = auto()

    def label(self):
        if self == ForceUnit.NEWTON:
            return "N"
        if self == ForceUnit.KILO_NEWTON:
            return "kN"
        if self == ForceUnit.MEGA_NEWTON:
            return "MN"
        if self == ForceUnit.TONNE:
            return "ton-force"