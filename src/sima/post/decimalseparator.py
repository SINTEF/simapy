# Generated with DecimalSeparator
# 
from enum import Enum
from enum import auto

class DecimalSeparator(Enum):
    """"""
    PERIOD = auto()
    COMMA = auto()

    def label(self):
        if self == DecimalSeparator.PERIOD:
            return "Period as decimal separator"
        if self == DecimalSeparator.COMMA:
            return "Comma as decimal separator"