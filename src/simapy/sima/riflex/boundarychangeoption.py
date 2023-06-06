# Generated with BoundaryChangeOption
# 
from enum import Enum
from enum import auto

class BoundaryChangeOption(Enum):
    """"""
    FREE = auto()
    FIXED_PRESCRIBED = auto()
    SLAVE = auto()

    def label(self):
        if self == BoundaryChangeOption.FREE:
            return "Free"
        if self == BoundaryChangeOption.FIXED_PRESCRIBED:
            return "Fixed or Prescribed"
        if self == BoundaryChangeOption.SLAVE:
            return "Slave"