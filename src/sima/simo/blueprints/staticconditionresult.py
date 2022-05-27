# 
# Generated with StaticConditionResultBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class StaticConditionResultBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="StaticConditionResult", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("bodyResults","sima/simo/BodyResult","",True,Dimension("*")))
        self.attributes.append(Attribute("header","string","",default=""))
        self.attributes.append(Attribute("dateTag","string","",default=""))
        self.attributes.append(Attribute("filepart","string","",default=""))
        self.attributes.append(Attribute("globalForces","boolean","",default=True))