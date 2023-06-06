# Generated with ArticulatedStructureType
# 
from enum import Enum
from enum import auto

class ArticulatedStructureType(Enum):
    """"""
    NRUN = auto()
    NONE = auto()
    TURRET = auto()
    HLA = auto()

    def label(self):
        if self == ArticulatedStructureType.NRUN:
            return "Predefined run"
        if self == ArticulatedStructureType.NONE:
            return "Member is fixed to its master"
        if self == ArticulatedStructureType.TURRET:
            return "Turret"
        if self == ArticulatedStructureType.HLA:
            return "Import from HLA"