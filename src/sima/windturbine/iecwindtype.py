# Generated with IECWindType
# 
from enum import Enum
from enum import auto

class IECWindType(Enum):
    """"""
    NTM = auto()
    ETM_1 = auto()
    ETM_2 = auto()
    ETM_3 = auto()
    EWM1_1 = auto()
    EWM1_2 = auto()
    EWM1_3 = auto()
    EWM50_1 = auto()
    EWM50_2 = auto()
    EWM50_3 = auto()

    def label(self):
        if self == IECWindType.NTM:
            return "Normal"
        if self == IECWindType.ETM_1:
            return "Extreme turbulence (turbine class 1)"
        if self == IECWindType.ETM_2:
            return "Extreme turbulence (turbine class 2)"
        if self == IECWindType.ETM_3:
            return "Extreme turbulence (turbine class 3)"
        if self == IECWindType.EWM1_1:
            return "Extreme 1-year wind (turbine class 1)"
        if self == IECWindType.EWM1_2:
            return "Extreme 1-year wind (turbine class 2)"
        if self == IECWindType.EWM1_3:
            return "Extreme 1-year wind (turbine class 3)"
        if self == IECWindType.EWM50_1:
            return "Extreme 50-year wind (turbine class 1)"
        if self == IECWindType.EWM50_2:
            return "Extreme 50-year wind (turbine class 2)"
        if self == IECWindType.EWM50_3:
            return "Extreme 50-year wind (turbine class 3)"