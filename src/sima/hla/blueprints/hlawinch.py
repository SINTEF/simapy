# 
# Generated with HLAWinchBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hlaobject import HLAObjectBlueprint

class HLAWinchBlueprint(HLAObjectBlueprint):
    """"""

    def __init__(self, name="HLAWinch", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("initialLength","number","Initial wire length at drum",default=0.0))
        self.add_attribute(Attribute("maximumSpeed","number","Max. run velocity for winch",default=0.0))
        self.add_attribute(Attribute("acceleration","number","Max. run acceleration for winch",default=0.0))
        self.add_attribute(Attribute("maximumLength","number","Max. wire length that can be added to drum",default=0.0))