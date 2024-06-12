# 
# Generated with TouchDownPointStorageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .linereference import LineReferenceBlueprint

class TouchDownPointStorageBlueprint(LineReferenceBlueprint):
    """"""

    def __init__(self, name="TouchDownPointStorage", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.add_attribute(Attribute("numberOfElements","integer","Additional bottom contact forces for a selected number of elements next to the TDP element",default=0))