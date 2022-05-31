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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("geometryPosition","sima/sima/Position","",True))
        self.attributes.append(Attribute("geometryFile","string","Geometry definition file",default=""))
        self.attributes.append(Attribute("transparency","number","Geometry transparency, [0-1], where 1 is full transparency.",default=0.0))