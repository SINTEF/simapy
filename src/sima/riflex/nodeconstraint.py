# Generated with NodeConstraint
# 
from enum import Enum
from enum import auto

class NodeConstraint(Enum):
    """"""
    FREE = auto()
    FIXED_PRESCRIBED = auto()
    SLAVE = auto()

    def label(self):
        if self == NodeConstraint.FREE:
            return "Free"
        if self == NodeConstraint.FIXED_PRESCRIBED:
            return "Fixed or Prescribed"
        if self == NodeConstraint.SLAVE:
            return "Slave"