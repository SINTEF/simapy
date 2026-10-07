# 
# Generated with DynamicNodalForcesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class DynamicNodalForcesBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DynamicNodalForces", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("_type","sima/riflex/ForceSpecificationType","Type of force specification"))
        self.add_attribute(Attribute("fileName","string","Time series file of nodal force components. The first line specifies the units; each following line gives a time instant followed by its force components."))
        self.add_attribute(BlueprintAttribute("items","sima/riflex/DynamicNodalForceItem","",True,Dimension("*")))