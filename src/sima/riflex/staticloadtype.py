# Generated with StaticLoadType
# 
from enum import Enum
from enum import auto

class StaticLoadType(Enum):
    """"""
    VOLU = auto()
    DISP = auto()
    SFOR = auto()
    CURR = auto()
    TENS = auto()
    ROLL = auto()
    PIPE = auto()
    ISTR = auto()
    FLOA = auto()
    FRIC = auto()
    SPRI = auto()
    BEND = auto()
    TEMP = auto()
    PRES = auto()
    MEMO = auto()
    BOUND = auto()
    WINCH = auto()
    GROW = auto()
    WIND = auto()

    def label(self):
        if self == StaticLoadType.VOLU:
            return "Volume Forces"
        if self == StaticLoadType.DISP:
            return "Specified Displacements"
        if self == StaticLoadType.SFOR:
            return "Specified Forces"
        if self == StaticLoadType.CURR:
            return "Current Forces"
        if self == StaticLoadType.TENS:
            return "Tension Contact Forces"
        if self == StaticLoadType.ROLL:
            return "Roller Contact Forces"
        if self == StaticLoadType.PIPE:
            return "Pipe-in-pipe contact forces"
        if self == StaticLoadType.ISTR:
            return "Initially pre-stressed segments"
        if self == StaticLoadType.FLOA:
            return "Body Forces"
        if self == StaticLoadType.FRIC:
            return "Activate bottom friction forces"
        if self == StaticLoadType.SPRI:
            return "Activate global springs"
        if self == StaticLoadType.BEND:
            return "Bending stiffness"
        if self == StaticLoadType.TEMP:
            return "Temperature variation"
        if self == StaticLoadType.PRES:
            return "Pressure variations"
        if self == StaticLoadType.MEMO:
            return "Activate material memory"
        if self == StaticLoadType.BOUND:
            return "Boundary Change"
        if self == StaticLoadType.WINCH:
            return "Winch variation"
        if self == StaticLoadType.GROW:
            return "Marine growth"
        if self == StaticLoadType.WIND:
            return "Wind force"