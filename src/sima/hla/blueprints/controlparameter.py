# 
# Generated with ControlParameterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.custom.blueprints.customcomponent import CustomComponentBlueprint

class ControlParameterBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="ControlParameter", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("label","string","",default=""))
        self.attributes.append(Attribute("tooltip","string","",default=""))
        self.attributes.append(Attribute("hlaObjectId","string","",default=""))