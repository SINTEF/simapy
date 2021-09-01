# Generated with LoadFormulation
# 
from enum import Enum
from enum import auto

class LoadFormulation(Enum):
    """"""
    MORISON = auto()
    MACCAMY_FUCHS = auto()
    POTN = auto()
    TVIV = auto()
    MORISON_PART_SUB = auto()
    NET = auto()
    NONE = auto()

    def label(self):
        if self == LoadFormulation.MORISON:
            return "Morison"
        if self == LoadFormulation.MACCAMY_FUCHS:
            return "MacCamy-Fuchs with quadratic drag"
        if self == LoadFormulation.POTN:
            return "Potential flow with quadratic drag load coefficients"
        if self == LoadFormulation.TVIV:
            return "Time domain VIV"
        if self == LoadFormulation.MORISON_PART_SUB:
            return "Morison partly submerged cross section"
        if self == LoadFormulation.NET:
            return "Net"
        if self == LoadFormulation.NONE:
            return "None"