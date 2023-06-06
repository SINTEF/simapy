# Generated with FilterLengthOption
# 
from enum import Enum
from enum import auto

class FilterLengthOption(Enum):
    """"""
    ROTOR = auto()
    WAKE = auto()

    def label(self):
        if self == FilterLengthOption.ROTOR:
            return "Rotor diameter"
        if self == FilterLengthOption.WAKE:
            return "Wake diameter"