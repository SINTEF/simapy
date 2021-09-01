# Generated with LevelStatisticsMethod
# 
from enum import Enum
from enum import auto

class LevelStatisticsMethod(Enum):
    """"""
    FROM_DISTRIBUTION = auto()
    FROM_EXTREMES = auto()

    def label(self):
        if self == LevelStatisticsMethod.FROM_DISTRIBUTION:
            return "From distribution"
        if self == LevelStatisticsMethod.FROM_EXTREMES:
            return "From extremes"