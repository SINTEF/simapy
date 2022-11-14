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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("_id","string","",default=None))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string","",default=None))
        self.add_attribute(EnumAttribute("_type","sima/hla/SurfaceType",""))
        self.add_attribute(Attribute("transparency","number","",default=0.0))
        self.add_attribute(Attribute("sizeX","number","",default=0.0))
        self.add_attribute(Attribute("sizeY","number","",default=0.0))