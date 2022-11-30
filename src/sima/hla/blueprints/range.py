# 
# Generated with RangeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class RangeBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="Range", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("min","number","",default=0.0))
        self.add_attribute(Attribute("max","number","",default=0.0))
        self.add_attribute(Attribute("automatic","boolean","",default=False))