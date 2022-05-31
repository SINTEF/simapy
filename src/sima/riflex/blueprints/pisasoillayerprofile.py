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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("topLevelSoilPosition","sima/riflex/TopLevelSoilPosition",""))
        self.attributes.append(Attribute("offsetSeafloorToTopSoil","number","Offset between seafloor and top of upper soil layer",default=0.0))
        self.attributes.append(BlueprintAttribute("soilLayers","sima/riflex/PisaSoilLayer","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("embeddedLines","sima/riflex/PisaLineItem","",True,Dimension("*")))