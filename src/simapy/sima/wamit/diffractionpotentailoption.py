# Generated with DiffractionPotentailOption
# 
from enum import Enum
from enum import auto

class DiffractionPotentailOption(Enum):
    """"""
    DIFFRACTION = auto()
    SCATTERING = auto()

    def label(self):
        if self == DiffractionPotentailOption.DIFFRACTION:
            return "Diffraction"
        if self == DiffractionPotentailOption.SCATTERING:
            return "Scattering"