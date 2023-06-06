# Generated with SignalAxis
# 
from enum import Enum
from enum import auto

class SignalAxis(Enum):
    """"""
    Y = auto()
    X = auto()

    def label(self):
        if self == SignalAxis.Y:
            return "Y-Axis"
        if self == SignalAxis.X:
            return "X-Axis"