# 
# Generated with HLASurfaceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hlaobject import HLAObjectBlueprint

class HLASurfaceBlueprint(HLAObjectBlueprint):
    """"""

    def __init__(self, name="HLASurface", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("_type","sima/hla/SurfaceType",""))
        self.attributes.append(Attribute("transparency","number","",default=0.0))
        self.attributes.append(Attribute("sizeX","number","",default=0.0))
        self.attributes.append(Attribute("sizeY","number","",default=0.0))