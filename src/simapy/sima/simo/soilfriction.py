# Generated with SoilFriction
# 
from enum import Enum
from enum import auto

class SoilFriction(Enum):
    """"""
    OPEN_COMPARTMENT = auto()
    SOIL_FRACTURE = auto()
    OPEN_COMPARTMENT_HORSLIDING = auto()

    def label(self):
        if self == SoilFriction.OPEN_COMPARTMENT:
            return "Open compartment"
        if self == SoilFriction.SOIL_FRACTURE:
            return "Soil fracture"
        if self == SoilFriction.OPEN_COMPARTMENT_HORSLIDING:
            return "Open compartment horizontal sliding"