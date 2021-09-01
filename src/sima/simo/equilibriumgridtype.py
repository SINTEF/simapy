# Generated with EquilibriumGridType
# 
from enum import Enum
from enum import auto

class EquilibriumGridType(Enum):
    """"""
    ROLL_AND_PITCH_ANGLES = auto()
    AZIMUTH_AND_ROTATION_ANGLES = auto()
    AZIMUTH_VECTOR_COMOPONENTS = auto()

    def label(self):
        if self == EquilibriumGridType.ROLL_AND_PITCH_ANGLES:
            return "Roll and pitch angles"
        if self == EquilibriumGridType.AZIMUTH_AND_ROTATION_ANGLES:
            return "Azimuth and rotation angles"
        if self == EquilibriumGridType.AZIMUTH_VECTOR_COMOPONENTS:
            return "Azimuth vector components"