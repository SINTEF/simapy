# Generated with FatigueCalculationOption
# 
from enum import Enum
from enum import auto

class FatigueCalculationOption(Enum):
    """"""
    DEFAULT = auto()
    RAINFLOW_COUNTING = auto()
    RAYLEIGH_DISTRIBUTION = auto()
    CONSTANT_STRESS_AMPLITUDE = auto()

    def label(self):
        if self == FatigueCalculationOption.DEFAULT:
            return "Default"
        if self == FatigueCalculationOption.RAINFLOW_COUNTING:
            return "Rainflow counting"
        if self == FatigueCalculationOption.RAYLEIGH_DISTRIBUTION:
            return "Rayleigh distribution"
        if self == FatigueCalculationOption.CONSTANT_STRESS_AMPLITUDE:
            return "Constant stress amplitude"