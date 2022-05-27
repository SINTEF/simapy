# 
# Generated with SoilCapacityElementBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SoilCapacityElementBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SoilCapacityElement", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("dCap","number","Penetration relative to ZCONT (positive upwards)",default=0.0))
        self.attributes.append(Attribute("soilFr","number","Soil capacity against failure at soil surface",default=0.0))
        self.attributes.append(Attribute("frcDep","number","Depth of each new soil failure",default=0.0))
        self.attributes.append(Attribute("pSuct","number","Suction pressure",default=0.0))