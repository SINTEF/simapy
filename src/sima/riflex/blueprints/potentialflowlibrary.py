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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("file","string","Potential flow library file",default=""))
        self.attributes.append(BlueprintAttribute("elements","sima/riflex/ElementReference","",True,Dimension("size","")))