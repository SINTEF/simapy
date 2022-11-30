# 
# Generated with DynamicLoadsBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DynamicLoadsBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DynamicLoads", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("dynamicNodalForces","sima/riflex/DynamicNodalForces","",True))
        self.add_attribute(BlueprintAttribute("dynamicCurrentVariation","sima/riflex/DynamicCurrentVariation","",True))
        self.add_attribute(BlueprintAttribute("rigidMoonpoolColumns","sima/riflex/RigidMoonpoolColumn","",True))