# 
# Generated with PisaSoilLayerProfileBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .soillayerprofile import SoilLayerProfileBlueprint

class PisaSoilLayerProfileBlueprint(SoilLayerProfileBlueprint):
    """"""

    def __init__(self, name="PisaSoilLayerProfile", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(EnumAttribute("topLevelSoilPosition","sima/riflex/TopLevelSoilPosition",""))
        self.add_attribute(Attribute("offsetSeafloorToTopSoil","number","Offset between seafloor and top of upper soil layer",default=0.0))
        self.add_attribute(BlueprintAttribute("soilLayers","sima/riflex/PisaSoilLayer","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("embeddedLines","sima/riflex/PisaLineItem","",True,Dimension("*")))