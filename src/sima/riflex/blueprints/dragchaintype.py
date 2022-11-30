# 
# Generated with DragChainTypeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .nodalcomponenttype import NodalComponentTypeBlueprint

class DragChainTypeBlueprint(NodalComponentTypeBlueprint):
    """"""

    def __init__(self, name="DragChainType", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("length","number","Drag chain length.",default=0.0))
        self.add_attribute(Attribute("unitWeight","number","Drag chain weight.",default=0.0))
        self.add_attribute(Attribute("friction","number","Chain / seafloor friction coefficient.",default=0.0))
        self.add_attribute(Attribute("cableLength","number","Cable length.",default=0.0))
        self.add_attribute(Attribute("cableWeight","number","Cable weight.",default=0.0))