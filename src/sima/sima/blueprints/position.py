# 
# Generated with PositionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .moao import MOAOBlueprint

class PositionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="Position", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("x","number","x position coordinate ",default=0.0))
        self.attributes.append(Attribute("y","number","y position coordinate ",default=0.0))
        self.attributes.append(Attribute("z","number","z position coordinate ",default=0.0))
        self.attributes.append(Attribute("rx","number","rotation about x-axis",default=0.0))
        self.attributes.append(Attribute("ry","number","rotation about y-axis",default=0.0))
        self.attributes.append(Attribute("rz","number","rotation about z-axis",default=0.0))