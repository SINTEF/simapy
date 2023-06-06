# Generated with KalmanLineTension
# 
from enum import Enum
from enum import auto

class KalmanLineTension(Enum):
    """"""
    NONE = auto()
    MEASUREMENTS = auto()
    STIFFNESS_MATRIX = auto()
    FULL_STIFFNESS_MATRIX = auto()
    STIFFNESS_MATRIX_ANCHOR_SYSTEM = auto()
    FORCES_FROM_SPECIFIED_LINES = auto()

    def label(self):
        if self == KalmanLineTension.NONE:
            return "None"
        if self == KalmanLineTension.MEASUREMENTS:
            return "Measurements"
        if self == KalmanLineTension.STIFFNESS_MATRIX:
            return "Stiffness matrix"
        if self == KalmanLineTension.FULL_STIFFNESS_MATRIX:
            return "Full stiffness matrix"
        if self == KalmanLineTension.STIFFNESS_MATRIX_ANCHOR_SYSTEM:
            return "Stiffness matrix for anchor system"
        if self == KalmanLineTension.FORCES_FROM_SPECIFIED_LINES:
            return "Forces from specified lines"