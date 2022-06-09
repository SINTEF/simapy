# Generated with ViscosityFilter
# 
from enum import Enum
from enum import auto

class ViscosityFilter(Enum):
    """"""
    MADSEN = auto()
    LARSEN = auto()
    KECK = auto()
    IEC19 = auto()

    def label(self):
        if self == ViscosityFilter.MADSEN:
            return "Based on Madsen"
        if self == ViscosityFilter.LARSEN:
            return "Based on Larsen"
        if self == ViscosityFilter.KECK:
            return "Based on Keck"
        if self == ViscosityFilter.IEC19:
            return "Based on IEC 61400-1:2019"