# 
# Generated with CurrentProfileBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class CurrentProfileBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CurrentProfile", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("globalXPosition","number","Global X-coordinate for this current profile",default=0.0))
        self.add_attribute(Attribute("globalYPosition","number","Global Y-coordinate for this current profile",default=0.0))
        self.add_attribute(BlueprintAttribute("items","sima/environment/CurrentItem","",True,Dimension("*")))