# Generated with AerodynamicDescriptionType
# 
from enum import Enum
from enum import auto

class AerodynamicDescriptionType(Enum):
    """"""
    DRAG = auto()

    def label(self):
        if self == AerodynamicDescriptionType.DRAG:
            return "Morison-like loading"