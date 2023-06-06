# Generated with ElongationCharacteristicType
# 
from enum import Enum
from enum import auto

class ElongationCharacteristicType(Enum):
    """"""
    STRESS_STRAIN = auto()
    TENSION_STRAIN = auto()
    FIBRE_ROPE = auto()

    def label(self):
        if self == ElongationCharacteristicType.STRESS_STRAIN:
            return "Stress-Strain"
        if self == ElongationCharacteristicType.TENSION_STRAIN:
            return "Tension-Strain"
        if self == ElongationCharacteristicType.FIBRE_ROPE:
            return "Fibre Rope Model"