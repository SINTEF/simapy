# Generated with TurbulenceModel
# 
from enum import Enum
from enum import auto

class TurbulenceModel(Enum):
    """"""
    IECKAI = auto()
    IECVKM = auto()

    def label(self):
        if self == TurbulenceModel.IECKAI:
            return "Kaimal"
        if self == TurbulenceModel.IECVKM:
            return "von Karman"