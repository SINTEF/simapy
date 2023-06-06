# Generated with ShearProfile
# 
from enum import Enum
from enum import auto

class ShearProfile(Enum):
    """"""
    NONE = auto()
    POWER_SHEAR_PROFILE = auto()
    LOGARITHMIC_SHEAR_PROFILE = auto()
    TABULATED_SHEAR_PROFILE = auto()

    def label(self):
        if self == ShearProfile.NONE:
            return "None"
        if self == ShearProfile.POWER_SHEAR_PROFILE:
            return "Power shear profile"
        if self == ShearProfile.LOGARITHMIC_SHEAR_PROFILE:
            return "Logarithmic shear profile"
        if self == ShearProfile.TABULATED_SHEAR_PROFILE:
            return "Tabulated shear profile"