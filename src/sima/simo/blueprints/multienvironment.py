# 
# Generated with MultiEnvironmentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.environment.blueprints.environment import EnvironmentBlueprint

class MultiEnvironmentBlueprint(EnvironmentBlueprint):
    """"""

    def __init__(self, name="MultiEnvironment", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("items","sima/simo/MultiEnvironmentItem","",True,Dimension("*")))