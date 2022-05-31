# 
# Generated with NonlinearBuoyancyCorrectionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class NonlinearBuoyancyCorrectionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="NonlinearBuoyancyCorrection", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("fileName","string","Name of geometry file ('.gdf'-file)",default=""))
        self.attributes.append(BlueprintAttribute("location","sima/sima/Point3","",True))
        self.attributes.append(Attribute("minZ","number","Minimum vertical range value to be used given in '.gdf' file system",default=0.0))
        self.attributes.append(Attribute("maxZ","number","Maximum vertical range value to be used given in '.gdf' file system",default=0.0))
        self.attributes.append(EnumAttribute("correctionMethod","sima/simo/NonlinearBuoyancyCorrectionMethod",""))