# Generated with CompensatorType
# 
from enum import Enum
from enum import auto

class CompensatorType(Enum):
    """"""
    GENERIC = auto()
    NOT_IMPLEMENTED = auto()

    def label(self):
        if self == CompensatorType.GENERIC:
            return "Generic model"
        if self == CompensatorType.NOT_IMPLEMENTED:
            return "Not implemented"