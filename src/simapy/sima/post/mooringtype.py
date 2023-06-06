# Generated with MooringType
# 
from enum import Enum
from enum import auto

class MooringType(Enum):
    """"""
    PERMANENT_MOORING = auto()
    MOBILE_MOORING = auto()

    def label(self):
        if self == MooringType.PERMANENT_MOORING:
            return "Permanent mooring"
        if self == MooringType.MOBILE_MOORING:
            return "Mobile mooring"