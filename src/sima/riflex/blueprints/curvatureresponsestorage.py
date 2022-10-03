# 
# Generated with CurvatureResponseStorageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class CurvatureResponseStorageBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CurvatureResponseStorage", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("storageStep","integer","Code for storage of internal forces. Storage for every <storage step> given.",default=1))
        self.attributes.append(EnumAttribute("format","sima/riflex/FileFormatCode","Format code for additional output of time series"))
        self.attributes.append(BlueprintAttribute("elements","sima/riflex/ElementReference","Specification of nodes for displacement storage",True,Dimension("*")))