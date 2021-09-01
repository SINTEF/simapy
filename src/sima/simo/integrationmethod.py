# Generated with IntegrationMethod
# 
from enum import Enum
from enum import auto

class IntegrationMethod(Enum):
    """"""
    RUNGE_KUTTA = auto()
    EULER = auto()

    def label(self):
        if self == IntegrationMethod.RUNGE_KUTTA:
            return "Runge Kutta"
        if self == IntegrationMethod.EULER:
            return "Euler"