# Generated with DPThrusterType
# 
from enum import Enum
from enum import auto

class DPThrusterType(Enum):
    """"""
    FIXED = auto()
    VARIABLE = auto()

    def label(self):
        if self == DPThrusterType.FIXED:
            return "Fixed direction"
        if self == DPThrusterType.VARIABLE:
            return "Variable direction"