# Generated with WaveParticleMethod
# 
from enum import Enum
from enum import auto

class WaveParticleMethod(Enum):
    """"""
    VELOCITY_AND_ACCELERATION = auto()
    NOT_INCLUDED = auto()
    VELOCITY = auto()
    VELOCITY_FIRST_AND_LAST_STRIP = auto()
    VELOCITY_AND_ACCELERATION_FIRST_AND_LAST_STRIP = auto()

    def label(self):
        if self == WaveParticleMethod.VELOCITY_AND_ACCELERATION:
            return "Velocity and acceleration"
        if self == WaveParticleMethod.NOT_INCLUDED:
            return "Not included"
        if self == WaveParticleMethod.VELOCITY:
            return "Velocity"
        if self == WaveParticleMethod.VELOCITY_FIRST_AND_LAST_STRIP:
            return "Velocity (first and last strip only)"
        if self == WaveParticleMethod.VELOCITY_AND_ACCELERATION_FIRST_AND_LAST_STRIP:
            return "Velocity and acceleration (first and last strip only)"