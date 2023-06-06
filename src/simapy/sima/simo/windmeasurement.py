# Generated with WindMeasurement
# 
from enum import Enum
from enum import auto

class WindMeasurement(Enum):
    """"""
    NO = auto()
    WITH_LP = auto()
    WITHOUT_LP = auto()

    def label(self):
        if self == WindMeasurement.NO:
            return "No"
        if self == WindMeasurement.WITH_LP:
            return "With LP"
        if self == WindMeasurement.WITHOUT_LP:
            return "Without LP"