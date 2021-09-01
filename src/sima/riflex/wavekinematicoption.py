# Generated with WaveKinematicOption
# 
from enum import Enum
from enum import auto

class WaveKinematicOption(Enum):
    """"""
    NODE = auto()
    DIFF = auto()
    WKFI = auto()

    def label(self):
        if self == WaveKinematicOption.NODE:
            return "Node step for calculating wave kinematics"
        if self == WaveKinematicOption.DIFF:
            return "Diffracted wave kinematic option at specific node"
        if self == WaveKinematicOption.WKFI:
            return "Wave kinematics time series reference"