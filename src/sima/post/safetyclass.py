# Generated with SafetyClass
# 
from enum import Enum
from enum import auto

class SafetyClass(Enum):
    """"""
    LOW = auto()
    NORMAL = auto()
    HIGH = auto()

    def label(self):
        if self == SafetyClass.LOW:
            return "Low"
        if self == SafetyClass.NORMAL:
            return "Normal"
        if self == SafetyClass.HIGH:
            return "High"