# Generated with YesNoOption
# 
from enum import Enum
from enum import auto

class YesNoOption(Enum):
    """"""
    NO = auto()
    YES = auto()

    def label(self):
        if self == YesNoOption.NO:
            return "No"
        if self == YesNoOption.YES:
            return "Yes"