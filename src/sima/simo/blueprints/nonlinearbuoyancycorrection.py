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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("fileName","string","Name of geometry file ('.gdf'-file)"))
        self.add_attribute(BlueprintAttribute("location","sima/sima/Point3","",True))
        self.add_attribute(Attribute("minZ","number","Minimum vertical range value to be used given in '.gdf' file system",default=0.0))
        self.add_attribute(Attribute("maxZ","number","Maximum vertical range value to be used given in '.gdf' file system",default=0.0))
        self.add_attribute(EnumAttribute("correctionMethod","sima/simo/NonlinearBuoyancyCorrectionMethod",""))