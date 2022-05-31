# 
# Generated with Vector3Blueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .moao import MOAOBlueprint

class Vector3Blueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="Vector3", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("x","number","X component",default=0.0))
        self.attributes.append(Attribute("y","number","Y component",default=0.0))
        self.attributes.append(Attribute("z","number","Z component",default=0.0))