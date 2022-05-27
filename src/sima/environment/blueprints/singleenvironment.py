# 
# Generated with SingleEnvironmentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .environment import EnvironmentBlueprint

class SingleEnvironmentBlueprint(EnvironmentBlueprint):
    """"""

    def __init__(self, name="SingleEnvironment", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("wave","sima/environment/Wave","",True))
        self.attributes.append(BlueprintAttribute("swell","sima/environment/Wave","",True))
        self.attributes.append(BlueprintAttribute("wind","sima/environment/Wind","",True))
        self.attributes.append(BlueprintAttribute("current","sima/environment/Current","",True))