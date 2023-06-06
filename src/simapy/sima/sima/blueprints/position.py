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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("x","number","x position coordinate ",default=0.0))
        self.add_attribute(Attribute("y","number","y position coordinate ",default=0.0))
        self.add_attribute(Attribute("z","number","z position coordinate ",default=0.0))
        self.add_attribute(Attribute("rx","number","rotation about x-axis",default=0.0))
        self.add_attribute(Attribute("ry","number","rotation about y-axis",default=0.0))
        self.add_attribute(Attribute("rz","number","rotation about z-axis",default=0.0))