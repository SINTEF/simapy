# Generated with IrregularWaveIndicator
# 
from enum import Enum
from enum import auto

class IrregularWaveIndicator(Enum):
    """"""
    NEW = auto()
    NONE = auto()

    def label(self):
        if self == IrregularWaveIndicator.NEW:
            return "Wave forces present"
        if self == IrregularWaveIndicator.NONE:
            return "No wave forces"