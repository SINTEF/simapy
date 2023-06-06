# Generated with VIVLoadType
# 
from enum import Enum
from enum import auto

class VIVLoadType(Enum):
    """"""
    CROSS_FLOW = auto()
    IN_LINE = auto()
    COMBINED = auto()

    def label(self):
        if self == VIVLoadType.CROSS_FLOW:
            return "Cross-flow VIV loads are applied"
        if self == VIVLoadType.IN_LINE:
            return "In-line VIV loads are applied"
        if self == VIVLoadType.COMBINED:
            return "Combined cross-flow and in-line VIV loads are applied"