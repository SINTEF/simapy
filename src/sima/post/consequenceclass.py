# Generated with ConsequenceClass
# 
from enum import Enum
from enum import auto

class ConsequenceClass(Enum):
    """"""
    CLASS_ONE = auto()
    CLASS_TWO = auto()
    CLASS_THREE = auto()

    def label(self):
        if self == ConsequenceClass.CLASS_ONE:
            return "Class 1"
        if self == ConsequenceClass.CLASS_TWO:
            return "Class 2"
        if self == ConsequenceClass.CLASS_THREE:
            return "Class 3"