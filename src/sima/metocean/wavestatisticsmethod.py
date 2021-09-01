# Generated with WaveStatisticsMethod
# 
from enum import Enum
from enum import auto

class WaveStatisticsMethod(Enum):
    """"""
    FROM_DISTRIBUTION = auto()
    FROM_CONTOUR = auto()

    def label(self):
        if self == WaveStatisticsMethod.FROM_DISTRIBUTION:
            return "From distribution"
        if self == WaveStatisticsMethod.FROM_CONTOUR:
            return "From contour data"