# 
# Generated with BumperPartBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BumperPartBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BumperPart", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("radius","number","diameter of bumper element",default=0.0))
        self.add_attribute(Attribute("stiffness","number","Bumper force stiffness, normal to elements",default=0.0))
        self.add_attribute(Attribute("damping","number","Damping",default=0.0))
        self.add_attribute(BlueprintAttribute("end1","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("end2","sima/sima/Point3","",True))