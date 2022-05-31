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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("length","number","Drag chain length.",default=0.0))
        self.attributes.append(Attribute("unitWeight","number","Drag chain weight.",default=0.0))
        self.attributes.append(Attribute("friction","number","Chain / seafloor friction coefficient.",default=0.0))
        self.attributes.append(Attribute("cableLength","number","Cable length.",default=0.0))
        self.attributes.append(Attribute("cableWeight","number","Cable weight.",default=0.0))