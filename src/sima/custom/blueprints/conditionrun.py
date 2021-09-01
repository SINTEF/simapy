# 
# Generated with ConditionRunBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .customcomponent import CustomComponentBlueprint

class ConditionRunBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="ConditionRun", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("condition","sima/sima/Condition","",False))
        self.attributes.append(Attribute("_type","string","",default=""))
        self.attributes.append(Attribute("addAllConditionTypes","boolean","",default=False))
        self.attributes.append(Attribute("addCustomLabel","boolean","",default=False))
        self.attributes.append(Attribute("label","string","",default=""))
        self.attributes.append(Attribute("addOpenView","boolean","",default=False))