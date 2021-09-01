# Generated with IterationType
# 
from enum import Enum
from enum import auto

class IterationType(Enum):
    """"""
    TRUE_NEWTON_RAPHSON = auto()
    MODIFIED_NEWTON_RAPHSON = auto()

    def label(self):
        if self == IterationType.TRUE_NEWTON_RAPHSON:
            return "True Newton-Raphson"
        if self == IterationType.MODIFIED_NEWTON_RAPHSON:
            return "Modified Newton-Raphson"