# 
# Generated with GrowthLevelBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class GrowthLevelBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="GrowthLevel", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("levelZCoordinate","number","Z coordinate of level given in global coordinate system",default=0.0))
        self.attributes.append(Attribute("thickness","number","Growth thickness at this level",default=0.0))
        self.attributes.append(Attribute("density","number","Growth density at this level",default=0.0))