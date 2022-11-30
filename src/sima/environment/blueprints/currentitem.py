# 
# Generated with CurrentItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class CurrentItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CurrentItem", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("level","number","Global z-coordinate of current level",default=0.0))
        self.add_attribute(Attribute("direction","number","Current propagation direction",default=0.0))
        self.add_attribute(Attribute("velocity","number","Current velocity",default=0.0))