# Generated with WakeFlowModel
# 
from enum import Enum
from enum import auto

class WakeFlowModel(Enum):
    """"""
    JIMENEZ = auto()
    BASTANKHAH = auto()

    def label(self):
        if self == WakeFlowModel.JIMENEZ:
            return "Jimenez"
        if self == WakeFlowModel.BASTANKHAH:
            return "Bastankhah"