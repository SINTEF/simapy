# 
# Generated with HLAPipeRouteBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hlaobject import HLAObjectBlueprint

class HLAPipeRouteBlueprint(HLAObjectBlueprint):
    """"""

    def __init__(self, name="HLAPipeRoute", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("routeFile","string","",default=""))
        self.attributes.append(Attribute("coordsUTM","string","",default='no'))
        self.attributes.append(Attribute("mapOnTerrain","string","",default='auto'))
        self.attributes.append(Attribute("routeWidth","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("color","sima/sima/SIMAColor","",False))
        self.attributes.append(BlueprintAttribute("routeWidthColor","sima/sima/SIMAColor","",False))