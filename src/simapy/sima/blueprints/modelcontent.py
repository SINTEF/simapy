# 
# Generated with ModelContentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from dmt.blueprints.entity import EntityBlueprint

class ModelContentBlueprint(EntityBlueprint):
    """"""

    def __init__(self, name="ModelContent", package_path="sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("header","sima/Header","",True))
        self.add_attribute(BlueprintAttribute("contents","system/SIMOS/Entity","",True,Dimension("*")))