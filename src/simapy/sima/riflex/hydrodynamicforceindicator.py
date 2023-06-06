# Generated with HydrodynamicForceIndicator
# 
from enum import Enum
from enum import auto

class HydrodynamicForceIndicator(Enum):
    """"""
    NO_FORCE_ITERATION_VELOCITIES = auto()
    NO_FORCE_ITERATION_ACCELERATION = auto()
    FORCE_ITERATION = auto()

    def label(self):
        if self == HydrodynamicForceIndicator.NO_FORCE_ITERATION_VELOCITIES:
            return "No force iteration (velocities at prev time step)"
        if self == HydrodynamicForceIndicator.NO_FORCE_ITERATION_ACCELERATION:
            return "No force iteration (velocities and acceleration at prev time step)"
        if self == HydrodynamicForceIndicator.FORCE_ITERATION:
            return "Force iteration"