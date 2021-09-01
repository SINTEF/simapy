# Generated with MaterialModel
# 
from enum import Enum
from enum import auto

class MaterialModel(Enum):
    """"""
    LINEAR_MATERIAL = auto()
    ELASTIC_PLASTIC = auto()
    STRAIN_STRESS_CURVE = auto()
    LINEAR_MATERIAL_INCLUDING_SHEAR = auto()

    def label(self):
        if self == MaterialModel.LINEAR_MATERIAL:
            return "Linear material"
        if self == MaterialModel.ELASTIC_PLASTIC:
            return "Elastic-plastic"
        if self == MaterialModel.STRAIN_STRESS_CURVE:
            return "Strain-stress curve"
        if self == MaterialModel.LINEAR_MATERIAL_INCLUDING_SHEAR:
            return "Linear material including shear"