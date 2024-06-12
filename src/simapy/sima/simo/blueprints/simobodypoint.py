# 
# Generated with SIMOBodyPointBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.namedobject import NamedObjectBlueprint
from .bodyforcecomponent import BodyForceComponentBlueprint

class SIMOBodyPointBlueprint(NamedObjectBlueprint,BodyForceComponentBlueprint):
    """"""

    def __init__(self, name="SIMOBodyPoint", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("winch","sima/simo/Winch","",True))
        self.add_attribute(BlueprintAttribute("tensioner","sima/simo/SIMOTensioner","",True))
        self.add_attribute(BlueprintAttribute("heaveCompensator","sima/simo/SIMOHeaveCompensator","",True))
        self.add_attribute(Attribute("x","number","X-coordinate of attachment point in body fixed (local) coordinate system",default=0.0))
        self.add_attribute(Attribute("y","number","Y-coordinate of attachment point in body fixed (local) coordinate system",default=0.0))
        self.add_attribute(Attribute("z","number","Z-coordinate of attachment point in body fixed (local) coordinate system",default=0.0))