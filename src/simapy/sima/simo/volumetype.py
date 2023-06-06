# Generated with VolumeType
# 
from enum import Enum
from enum import auto

class VolumeType(Enum):
    """"""
    CONE = auto()
    BOX = auto()

    def label(self):
        if self == VolumeType.CONE:
            return "Cone"
        if self == VolumeType.BOX:
            return "Box"