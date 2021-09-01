# Generated with DepthDistribution
# 
from enum import Enum
from enum import auto

class DepthDistribution(Enum):
    """"""
    EQUIDISTANT = auto()
    QUADRATIC = auto()
    WAVE = auto()

    def label(self):
        if self == DepthDistribution.EQUIDISTANT:
            return "Equidistant"
        if self == DepthDistribution.QUADRATIC:
            return "Quadratic"
        if self == DepthDistribution.WAVE:
            return "Wave"