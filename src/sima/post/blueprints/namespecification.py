# 
# Generated with NameSpecificationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .pathspecification import PathSpecificationBlueprint

class NameSpecificationBlueprint(PathSpecificationBlueprint):
    """"""

    def __init__(self, name="NameSpecification", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("path","string","",default=""))
        self.attributes.append(Attribute("name","string","",default=""))