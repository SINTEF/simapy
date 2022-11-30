# 
# Generated with NonLinearHydrostaticStiffnessBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class NonLinearHydrostaticStiffnessBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="NonLinearHydrostaticStiffness", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("geometryPosition","sima/sima/Position","",True))
        self.add_attribute(Attribute("geometryFile","string","Geometry definition file"))
        self.add_attribute(Attribute("transparency","number","Geometry transparency, [0-1], where 1 is full transparency.",default=0.0))