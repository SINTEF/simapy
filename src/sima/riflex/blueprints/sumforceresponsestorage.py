# 
# Generated with SumForceResponseStorageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SumForceResponseStorageBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SumForceResponseStorage", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("storageStep","integer","Code for storage of the sum of forces. Storage for every <storage step> given.",default=1))
        self.add_attribute(EnumAttribute("format","sima/riflex/AdditionalFileFormatCode","Format code for additional output of time series"))
        self.add_attribute(BlueprintAttribute("elements","sima/riflex/ElementReference","Specification of nodes for displacement storage",True,Dimension("*")))