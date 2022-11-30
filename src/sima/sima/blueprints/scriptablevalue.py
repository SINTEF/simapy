# 
# Generated with ScriptableValueBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class ScriptableValueBlueprint(EntityBlueprint):
    """"""

    def __init__(self, name="ScriptableValue", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("script","string",""))
        self.add_attribute(BlueprintAttribute("dependencies","sima/sima/Dependency","",True,Dimension("*")))
        self.add_attribute(Attribute("cyclic","boolean","",default=False))
        self.add_attribute(Attribute("feature","string",""))
        self.add_attribute(Attribute("index","integer","",default=-1))