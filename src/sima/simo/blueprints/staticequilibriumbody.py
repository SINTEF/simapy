# 
# Generated with StaticEquilibriumBodyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class StaticEquilibriumBodyBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="StaticEquilibriumBody", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("body","sima/simo/SIMOBody","Selected body to compute equilibrium for",False))
        self.add_attribute(Attribute("x","number","Excursion along global X axis",default=1.0))
        self.add_attribute(Attribute("y","number","Excursion along global Y axis",default=1.0))
        self.add_attribute(Attribute("z","number","Excursion along global Z axis",default=1.0))
        self.add_attribute(Attribute("rx","number","Excursion of rotation about global X axis",default=1.0))
        self.add_attribute(Attribute("ry","number","Excursion of rotation about global Y axis",default=1.0))
        self.add_attribute(Attribute("rz","number","Excursion of rotation about global Z axis",default=1.0))