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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("routeFile","string",""))
        self.add_attribute(Attribute("coordsUTM","string","",default='no'))
        self.add_attribute(Attribute("mapOnTerrain","string","",default='auto'))
        self.add_attribute(Attribute("routeWidth","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("color","sima/sima/SIMAColor","",False))
        self.add_attribute(BlueprintAttribute("routeWidthColor","sima/sima/SIMAColor","",False))