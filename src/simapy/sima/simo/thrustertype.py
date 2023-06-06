# Generated with ThrusterType
# 
from enum import Enum
from enum import auto

class ThrusterType(Enum):
    """"""
    FIXED_CONVENTIONAL = auto()
    FIXED_DUCTED = auto()
    FIXED_TUNNEL = auto()
    ROTATABLE_CONVENTIONAL = auto()
    ROTATABLE_DUCTED = auto()
    OPEN_MAIN_PROPELLER = auto()
    DUCTED_MAIN_PROPELLER = auto()

    def label(self):
        if self == ThrusterType.FIXED_CONVENTIONAL:
            return "Fixed conventional"
        if self == ThrusterType.FIXED_DUCTED:
            return "Fixed ducted"
        if self == ThrusterType.FIXED_TUNNEL:
            return "Fixed tunnel"
        if self == ThrusterType.ROTATABLE_CONVENTIONAL:
            return "Rotatable conventional"
        if self == ThrusterType.ROTATABLE_DUCTED:
            return "Rotatable ducted"
        if self == ThrusterType.OPEN_MAIN_PROPELLER:
            return "Open main propeller"
        if self == ThrusterType.DUCTED_MAIN_PROPELLER:
            return "Ducted main propeller"