# 
# Generated with HLAActivePipeRouteBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hlaobject import HLAObjectBlueprint

class HLAActivePipeRouteBlueprint(HLAObjectBlueprint):
    """"""

    def __init__(self, name="HLAActivePipeRoute", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("fileName","string","",default=""))
        self.attributes.append(Attribute("mapOnTerrain","string","",default=""))
        self.attributes.append(BlueprintAttribute("color","sima/sima/SIMAColor","",False))