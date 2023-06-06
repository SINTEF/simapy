# Generated with SignalType
# 
from enum import Enum
from enum import auto

class SignalType(Enum):
    """"""
    CONSTANT = auto()
    EQUIDISTANT = auto()
    NONEQUIDISTANT = auto()
    TEXT = auto()
    TEXTARRAY = auto()

    def label(self):
        if self == SignalType.CONSTANT:
            return "Constant number"
        if self == SignalType.EQUIDISTANT:
            return "Equidistant signal"
        if self == SignalType.NONEQUIDISTANT:
            return "Non-equidistant signal"
        if self == SignalType.TEXT:
            return "Text"
        if self == SignalType.TEXTARRAY:
            return "Array of text"