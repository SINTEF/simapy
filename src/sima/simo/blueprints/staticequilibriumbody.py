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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("body","sima/simo/SIMOBody","Selected body to compute equilibrium for",False))
        self.attributes.append(Attribute("x","number","Excursion along global X axis",default=1.0))
        self.attributes.append(Attribute("y","number","Excursion along global Y axis",default=1.0))
        self.attributes.append(Attribute("z","number","Excursion along global Z axis",default=1.0))
        self.attributes.append(Attribute("rx","number","Excursion of rotation about global X axis",default=1.0))
        self.attributes.append(Attribute("ry","number","Excursion of rotation about global Y axis",default=1.0))
        self.attributes.append(Attribute("rz","number","Excursion of rotation about global Z axis",default=1.0))