# Generated with GeneratorTorqueFault
# 
from enum import Enum
from enum import auto

class GeneratorTorqueFault(Enum):
    """"""
    NONE = auto()
    LOSS = auto()
    BACKUP = auto()

    def label(self):
        if self == GeneratorTorqueFault.NONE:
            return "No generator torque fault"
        if self == GeneratorTorqueFault.LOSS:
            return "Total loss of generator torque"
        if self == GeneratorTorqueFault.BACKUP:
            return "Backup power - torque follows scaled torque control"