# Generated with ControlParameter
# 
from enum import Enum
from enum import auto

class ControlParameter(Enum):
    """"""
    ON = auto()
    OFF = auto()

    def label(self):
        if self == ControlParameter.ON:
            return "On"
        if self == ControlParameter.OFF:
            return "Off"