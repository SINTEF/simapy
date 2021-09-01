# 
# Generated with MultiFeatureDependencyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .dependency import DependencyBlueprint

class MultiFeatureDependencyBlueprint(DependencyBlueprint):
    """"""

    def __init__(self, name="MultiFeatureDependency", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("object","sima/sima/MOAO","",False))
        self.attributes.append(Attribute("feature","string","",default=""))
        self.attributes.append(BlueprintAttribute("root","sima/sima/MOAO","",False))