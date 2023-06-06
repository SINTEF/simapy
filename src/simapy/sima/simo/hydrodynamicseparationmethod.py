# Generated with HydrodynamicSeparationMethod
# 
from enum import Enum
from enum import auto

class HydrodynamicSeparationMethod(Enum):
    """"""
    BW2_FILTERING = auto()
    NLP_FILTERING = auto()
    NONE = auto()

    def label(self):
        if self == HydrodynamicSeparationMethod.BW2_FILTERING:
            return "2nd Order Butterworth Filter"
        if self == HydrodynamicSeparationMethod.NLP_FILTERING:
            return "Non-Linearity Pass Filter"
        if self == HydrodynamicSeparationMethod.NONE:
            return "No estimation"