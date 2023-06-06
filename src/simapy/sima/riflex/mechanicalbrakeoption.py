# Generated with MechanicalBrakeOption
# 
from enum import Enum
from enum import auto

class MechanicalBrakeOption(Enum):
    """"""
    NONE = auto()
    BRAKE = auto()

    def label(self):
        if self == MechanicalBrakeOption.NONE:
            return "No mechanical brake"
        if self == MechanicalBrakeOption.BRAKE:
            return "Mechanical brake (linear damping)"