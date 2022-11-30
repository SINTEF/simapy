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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("wave","sima/environment/Wave","",True))
        self.add_attribute(BlueprintAttribute("swell","sima/environment/Wave","",True))
        self.add_attribute(BlueprintAttribute("wind","sima/environment/Wind","",True))
        self.add_attribute(BlueprintAttribute("current","sima/environment/Current","",True))