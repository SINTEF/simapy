# 
# Generated with HLAInitialViewpointBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hlaviewpoint import HLAViewpointBlueprint

class HLAInitialViewpointBlueprint(HLAViewpointBlueprint):
    """"""

    def __init__(self, name="HLAInitialViewpoint", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))