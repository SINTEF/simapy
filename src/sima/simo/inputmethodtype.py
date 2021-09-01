# Generated with InputMethodType
# 
from enum import Enum
from enum import auto

class InputMethodType(Enum):
    """"""
    TENSION = auto()
    ANCHORDIR = auto()
    ANCHORPOS = auto()

    def label(self):
        if self == InputMethodType.TENSION:
            return "Tension"
        if self == InputMethodType.ANCHORDIR:
            return "Anchor direction"
        if self == InputMethodType.ANCHORPOS:
            return "Anchor position"