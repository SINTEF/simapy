# 
# Generated with MoonpoolColumnItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class MoonpoolColumnItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="MoonpoolColumnItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("body","sima/sima/Body","",False))
        self.attributes.append(Attribute("lowerZ","number","Lower Z limit (local vessel system)",default=0.0))
        self.attributes.append(Attribute("upperZ","number","Upper Z limit (local vessel system)",default=0.0))
        self.attributes.append(BlueprintAttribute("lineReferences","sima/riflex/LineReference","",True,Dimension("*")))