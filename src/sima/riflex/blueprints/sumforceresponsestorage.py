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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("storageStep","integer","Code for storage of the sum of forces. Storage for every <storage step> given.",default=1))
        self.attributes.append(EnumAttribute("format","sima/riflex/AdditionalFileFormatCode","Format code for additional output of time series"))
        self.attributes.append(BlueprintAttribute("elements","sima/riflex/ElementReference","Specification of nodes for displacement storage",True,Dimension("*")))