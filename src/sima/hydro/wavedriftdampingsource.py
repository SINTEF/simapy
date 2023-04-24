# Generated with WaveDriftDampingSource
# 
from enum import Enum
from enum import auto

class WaveDriftDampingSource(Enum):
    """"""
    INPUT = auto()
    QTF = auto()
    WAVEDRIFTFORCE = auto()

    def label(self):
        if self == WaveDriftDampingSource.INPUT:
            return "Input"
        if self == WaveDriftDampingSource.QTF:
            return "QTF"
        if self == WaveDriftDampingSource.WAVEDRIFTFORCE:
            return "WaveDriftForce"