# 
# Generated with HLAForceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hlaobject import HLAObjectBlueprint

class HLAForceBlueprint(HLAObjectBlueprint):
    """"""

    def __init__(self, name="HLAForce", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("fx","number","",default=0.0))
        self.add_attribute(Attribute("fy","number","",default=0.0))
        self.add_attribute(Attribute("fz","number","",default=0.0))
        self.add_attribute(Attribute("mx","number","",default=0.0))
        self.add_attribute(Attribute("my","number","",default=0.0))
        self.add_attribute(Attribute("mz","number","",default=0.0))