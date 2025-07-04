# 
# Generated with RegularCurrentFromFileBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .current import CurrentBlueprint

class RegularCurrentFromFileBlueprint(CurrentBlueprint):
    """"""

    def __init__(self, name="RegularCurrentFromFile", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("fileName","string","Name of external file with specified current data"))