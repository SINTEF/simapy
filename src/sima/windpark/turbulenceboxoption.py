# Generated with TurbulenceBoxOption
# 
from enum import Enum
from enum import auto

class TurbulenceBoxOption(Enum):
    """"""
    DTUMANN = auto()
    TURBSIM = auto()

    def label(self):
        if self == TurbulenceBoxOption.DTUMANN:
            return "DTU Mann"
        if self == TurbulenceBoxOption.TURBSIM:
            return "TurbSim"