# 
# Generated with ExternalControlSystemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ExternalControlSystemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ExternalControlSystem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("intParameters","sima/simo/NamedIntParameter","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("doubleParameters","sima/simo/NamedDoubleParameter","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stringParameters","sima/simo/NamedStringParameter","",True,Dimension("*")))