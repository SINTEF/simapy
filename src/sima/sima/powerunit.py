# Generated with PowerUnit
# 
from enum import Enum
from enum import auto

class PowerUnit(Enum):
    """"""
    WATT = auto()
    KILO_WATT = auto()
    MEGA_WATT = auto()

    def label(self):
        if self == PowerUnit.WATT:
            return "W"
        if self == PowerUnit.KILO_WATT:
            return "kW"
        if self == PowerUnit.MEGA_WATT:
            return "MW"