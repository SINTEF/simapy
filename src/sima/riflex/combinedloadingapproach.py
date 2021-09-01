# Generated with CombinedLoadingApproach
# 
from enum import Enum
from enum import auto

class CombinedLoadingApproach(Enum):
    """"""
    LRFD = auto()
    WSD = auto()

    def label(self):
        if self == CombinedLoadingApproach.LRFD:
            return "LRFD"
        if self == CombinedLoadingApproach.WSD:
            return "WSD"