# 
# Generated with FileActionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .customcomponent import CustomComponentBlueprint

class FileActionBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="FileAction", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("_id","string","",default=None))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("label","string","",default=None))
        self.add_attribute(Attribute("tooltip","string","",default=None))
        self.add_attribute(Attribute("path","string","Path to the input file.",default=None))