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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("x","number","X component",default=0.0))
        self.add_attribute(Attribute("y","number","Y component",default=0.0))
        self.add_attribute(Attribute("z","number","Z component",default=0.0))