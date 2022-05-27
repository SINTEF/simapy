# 
# Generated with DynamicWinchVariationItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DynamicWinchVariationItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DynamicWinchVariationItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("winch","sima/riflex/ARWinch","",False))
        self.attributes.append(Attribute("startTime","number","Start time for winching",default=0.0))
        self.attributes.append(Attribute("endTime","number","End time for winching",default=0.0))
        self.attributes.append(Attribute("velocity","number","Winch velocity",default=0.0))