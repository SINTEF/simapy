# 
# Generated with Regular3DBottomBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class Regular3DBottomBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="Regular3DBottom", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("fileName","string","File with seabed geometry data"))
        self.add_attribute(Attribute("x","number","",default=0.0))
        self.add_attribute(Attribute("y","number","",default=0.0))
        self.add_attribute(Attribute("zos","number","Z-coordinate of the origin of the seabed file reference system, in the global reference system",default=0.0))
        self.add_attribute(Attribute("angos","number","Angle between the X-axis of the seabed file reference system and the X-axis of the global reference system",default=0.0))