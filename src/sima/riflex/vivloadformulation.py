# Generated with VIVLoadFormulation
# 
from enum import Enum
from enum import auto

class VIVLoadFormulation(Enum):
    """"""
    CROSSFLOW_VIV_ONLY = auto()
    CROSSFLOW_INDUCED_INLINE = auto()
    CROSSFLOW_INLINE_SEPARATE = auto()
    INLINE_VIV_ONLY = auto()

    def label(self):
        if self == VIVLoadFormulation.CROSSFLOW_VIV_ONLY:
            return "Cross-flow VIV loads only"
        if self == VIVLoadFormulation.CROSSFLOW_INDUCED_INLINE:
            return "Cross-flow loads and cross-flow induced in-line loads"
        if self == VIVLoadFormulation.CROSSFLOW_INLINE_SEPARATE:
            return "Cross-flow loads and in-line loads calculated separately"
        if self == VIVLoadFormulation.INLINE_VIV_ONLY:
            return "In-line VIV loads only"