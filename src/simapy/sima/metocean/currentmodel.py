# Generated with CurrentModel
# 
from enum import Enum
from enum import auto

class CurrentModel(Enum):
    """"""
    FROM_INPUT = auto()
    FROM_WIND_VELOCITY = auto()

    def label(self):
        if self == CurrentModel.FROM_INPUT:
            return "From input data"
        if self == CurrentModel.FROM_WIND_VELOCITY:
            return "From wind velocity"