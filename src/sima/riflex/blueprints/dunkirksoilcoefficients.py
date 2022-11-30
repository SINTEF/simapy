# 
# Generated with DunkirkSoilCoefficientsBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DunkirkSoilCoefficientsBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DunkirkSoilCoefficients", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("xu","sima/riflex/DunkirkSoilCoefficientsItem","",True))
        self.add_attribute(BlueprintAttribute("k","sima/riflex/DunkirkSoilCoefficientsItem","",True))
        self.add_attribute(BlueprintAttribute("n","sima/riflex/DunkirkSoilCoefficientsItem","",True))
        self.add_attribute(BlueprintAttribute("yu","sima/riflex/DunkirkSoilCoefficientsItem","",True))