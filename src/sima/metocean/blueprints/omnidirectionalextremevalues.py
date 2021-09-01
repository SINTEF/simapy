# 
# Generated with OmniDirectionalExtremeValuesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .levelextreme import LevelExtremeBlueprint

class OmniDirectionalExtremeValuesBlueprint(LevelExtremeBlueprint):
    """"""

    def __init__(self, name="OmniDirectionalExtremeValues", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("level","number","",default=0.0))
        self.attributes.append(Attribute("duration","number","",default=0.0))
        self.attributes.append(Attribute("probability","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("extremeValues","sima/metocean/ExtremeValue","",True,Dimension("size","")))