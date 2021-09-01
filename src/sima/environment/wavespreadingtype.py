# Generated with WaveSpreadingType
# 
from enum import Enum
from enum import auto

class WaveSpreadingType(Enum):
    """"""
    UNIDIRECTIONAL = auto()
    COSFUNCTION = auto()

    def label(self):
        if self == WaveSpreadingType.UNIDIRECTIONAL:
            return "Unidirectional"
        if self == WaveSpreadingType.COSFUNCTION:
            return "Cos function"