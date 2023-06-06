# Generated with LimitStateCategory
# 
from enum import Enum
from enum import auto

class LimitStateCategory(Enum):
    """"""
    SLS = auto()
    ULS = auto()
    ALS = auto()

    def label(self):
        if self == LimitStateCategory.SLS:
            return "SLS"
        if self == LimitStateCategory.ULS:
            return "ULS"
        if self == LimitStateCategory.ALS:
            return "ALS"