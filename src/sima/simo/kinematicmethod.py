# Generated with KinematicMethod
# 
from enum import Enum
from enum import auto

class KinematicMethod(Enum):
    """"""
    FFT = auto()
    COSINE = auto()

    def label(self):
        if self == KinematicMethod.FFT:
            return "FFT"
        if self == KinematicMethod.COSINE:
            return "Cosine"