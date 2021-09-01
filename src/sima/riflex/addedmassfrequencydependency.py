# Generated with AddedMassFrequencyDependency
# 
from enum import Enum
from enum import auto

class AddedMassFrequencyDependency(Enum):
    """"""
    FREQUENCY_ADDED_MASS = auto()
    STILL_WATER_ADDED_MASS = auto()
    TRANSITIONAL_ADDED_MASS = auto()

    def label(self):
        if self == AddedMassFrequencyDependency.FREQUENCY_ADDED_MASS:
            return "Use frequency-dependent added mass for all modes"
        if self == AddedMassFrequencyDependency.STILL_WATER_ADDED_MASS:
            return "Use constant still-water added mass for all modes"
        if self == AddedMassFrequencyDependency.TRANSITIONAL_ADDED_MASS:
            return "Transition from frequency-dependent to still-water added mass"