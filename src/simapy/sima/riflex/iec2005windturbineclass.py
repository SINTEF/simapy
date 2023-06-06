# Generated with IEC2005WindTurbineClass
# 
from enum import Enum
from enum import auto

class IEC2005WindTurbineClass(Enum):
    """"""
    NONE = auto()
    IA = auto()
    IIA = auto()
    IIIA = auto()
    IB = auto()
    IIB = auto()
    IIIB = auto()
    IC = auto()
    IIC = auto()
    IIIC = auto()
    S = auto()

    def label(self):
        if self == IEC2005WindTurbineClass.NONE:
            return "None"
        if self == IEC2005WindTurbineClass.IA:
            return "IA"
        if self == IEC2005WindTurbineClass.IIA:
            return "IIA"
        if self == IEC2005WindTurbineClass.IIIA:
            return "IIIA"
        if self == IEC2005WindTurbineClass.IB:
            return "IB"
        if self == IEC2005WindTurbineClass.IIB:
            return "IIB"
        if self == IEC2005WindTurbineClass.IIIB:
            return "IIIB"
        if self == IEC2005WindTurbineClass.IC:
            return "IC"
        if self == IEC2005WindTurbineClass.IIC:
            return "IIC"
        if self == IEC2005WindTurbineClass.IIIC:
            return "IIIC"
        if self == IEC2005WindTurbineClass.S:
            return "S"