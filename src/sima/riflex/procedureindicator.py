# Generated with ProcedureIndicator
# 
from enum import Enum
from enum import auto

class ProcedureIndicator(Enum):
    """"""
    NEWMARK = auto()
    WILSON = auto()

    def label(self):
        if self == ProcedureIndicator.NEWMARK:
            return "Newmark"
        if self == ProcedureIndicator.WILSON:
            return "Wilson"