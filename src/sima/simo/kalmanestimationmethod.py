# Generated with KalmanEstimationMethod
# 
from enum import Enum
from enum import auto

class KalmanEstimationMethod(Enum):
    """"""
    CURRENT = auto()
    FORCE = auto()

    def label(self):
        if self == KalmanEstimationMethod.CURRENT:
            return "Current"
        if self == KalmanEstimationMethod.FORCE:
            return "Force"