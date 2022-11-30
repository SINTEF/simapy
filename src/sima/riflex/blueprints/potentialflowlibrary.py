# 
# Generated with PotentialFlowLibraryBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class PotentialFlowLibraryBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="PotentialFlowLibrary", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("file","string","Potential flow library file"))
        self.add_attribute(BlueprintAttribute("elements","sima/riflex/ElementReference","",True,Dimension("*")))