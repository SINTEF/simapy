# Generated with WorkflowSetInput
# 
from enum import Enum
from enum import auto

class WorkflowSetInput(Enum):
    """"""
    MANUAL = auto()
    FILE = auto()
    INPUT = auto()

    def label(self):
        if self == WorkflowSetInput.MANUAL:
            return "Manual input"
        if self == WorkflowSetInput.FILE:
            return "From file"
        if self == WorkflowSetInput.INPUT:
            return "From input"