# Generated with WindTurbineLoadOption
# 
from enum import Enum
from enum import auto

class WindTurbineLoadOption(Enum):
    """"""
    INCLUDE = auto()
    EXCLUDE = auto()

    def label(self):
        if self == WindTurbineLoadOption.INCLUDE:
            return "Include wind moment"
        if self == WindTurbineLoadOption.EXCLUDE:
            return "Exclude wind moment"