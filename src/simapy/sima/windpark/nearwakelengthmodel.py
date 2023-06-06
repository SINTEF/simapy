# Generated with NearWakeLengthModel
# 
from enum import Enum
from enum import auto

class NearWakeLengthModel(Enum):
    """"""
    ROTOR_DIAMETERS = auto()
    VERMEULEN = auto()
    SORENSEN = auto()

    def label(self):
        if self == NearWakeLengthModel.ROTOR_DIAMETERS:
            return "Near length model 2 rotor diameters"
        if self == NearWakeLengthModel.VERMEULEN:
            return "Near length model based on Vermeulen"
        if self == NearWakeLengthModel.SORENSEN:
            return "Near length model based on Sorensen"