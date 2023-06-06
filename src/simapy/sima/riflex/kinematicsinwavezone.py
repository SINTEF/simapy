# Generated with KinematicsInWaveZone
# 
from enum import Enum
from enum import auto

class KinematicsInWaveZone(Enum):
    """"""
    MEAN_WATER_LEVEL = auto()
    STRETCHING_COMPRESSION = auto()
    MOVING_POTENTIAL = auto()
    CONSTANT_POTENTIAL = auto()
    SECOND_ORDER = auto()

    def label(self):
        if self == KinematicsInWaveZone.MEAN_WATER_LEVEL:
            return "Mean water level"
        if self == KinematicsInWaveZone.STRETCHING_COMPRESSION:
            return "Stretching and compression of wave potential"
        if self == KinematicsInWaveZone.MOVING_POTENTIAL:
            return "Moving the potential to actual surface"
        if self == KinematicsInWaveZone.CONSTANT_POTENTIAL:
            return "Keeping the potential constant from mean water level to wave surface"
        if self == KinematicsInWaveZone.SECOND_ORDER:
            return "Second order wave with integration of wave forces to wave surface"