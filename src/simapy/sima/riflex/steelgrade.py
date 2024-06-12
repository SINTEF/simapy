# Generated with SteelGrade
# 
from enum import Enum
from enum import auto

class SteelGrade(Enum):
    """"""
    R3 = auto()
    R3S = auto()
    R4 = auto()
    R4S = auto()
    R5 = auto()

    def label(self):
        if self == SteelGrade.R3:
            return "R3"
        if self == SteelGrade.R3S:
            return "R3S"
        if self == SteelGrade.R4:
            return "R4"
        if self == SteelGrade.R4S:
            return "R4S"
        if self == SteelGrade.R5:
            return "R5"