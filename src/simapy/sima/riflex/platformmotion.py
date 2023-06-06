# Generated with PlatformMotion
# 
from enum import Enum
from enum import auto

class PlatformMotion(Enum):
    """"""
    GENERATED = auto()
    NO_MOTIONS = auto()
    SPECIFIED = auto()

    def label(self):
        if self == PlatformMotion.GENERATED:
            return "Generated motions"
        if self == PlatformMotion.NO_MOTIONS:
            return "No motions"
        if self == PlatformMotion.SPECIFIED:
            return "Specified motions"