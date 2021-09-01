# 
# Generated with SectorExtremeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SectorExtremeBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SectorExtreme", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("sector","number","",default=0.0))
        self.attributes.append(Attribute("probability","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("extremeValues","sima/metocean/ExtremeValue","",True,Dimension("size","")))