# Generated with InputReferenceSystem
# 
from enum import Enum
from enum import auto

class InputReferenceSystem(Enum):
    """"""
    METOCEAN = auto()
    SIMA = auto()

    def label(self):
        if self == InputReferenceSystem.METOCEAN:
            return "Metocean"
        if self == InputReferenceSystem.SIMA:
            return "SIMA"