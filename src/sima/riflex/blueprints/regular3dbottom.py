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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("fileName","string","File with seabed geometry data",default=""))
        self.attributes.append(Attribute("x","number","",default=0.0))
        self.attributes.append(Attribute("y","number","",default=0.0))
        self.attributes.append(Attribute("zos","number","Z-coordinate of the origin of the seabed file reference system, in the global reference system",default=0.0))
        self.attributes.append(Attribute("angos","number","Angle between the X-axis of the seabed file reference system and the X-axis of the global reference system",default=0.0))