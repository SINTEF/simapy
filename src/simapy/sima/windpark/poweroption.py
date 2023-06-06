# Generated with PowerOption
# 
from enum import Enum
from enum import auto

class PowerOption(Enum):
    """"""
    COMP = auto()
    SKIP = auto()

    def label(self):
        if self == PowerOption.COMP:
            return "Compute"
        if self == PowerOption.SKIP:
            return "Skip"