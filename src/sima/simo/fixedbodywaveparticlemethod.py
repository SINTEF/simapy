# Generated with FixedBodyWaveParticleMethod
# 
from enum import Enum
from enum import auto

class FixedBodyWaveParticleMethod(Enum):
    """"""
    NOT_INCLUDED = auto()
    VELOCITY_ONLY = auto()
    VELOCITY_AND_ACCELERATION = auto()

    def label(self):
        if self == FixedBodyWaveParticleMethod.NOT_INCLUDED:
            return "Not included"
        if self == FixedBodyWaveParticleMethod.VELOCITY_ONLY:
            return "Velocity only"
        if self == FixedBodyWaveParticleMethod.VELOCITY_AND_ACCELERATION:
            return "Velocity and acceleration"