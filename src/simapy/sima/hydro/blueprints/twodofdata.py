# 
# Generated with TwoDofDataBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class TwoDofDataBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="TwoDofData", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("dof1","sima/hydro/DOF",""))
        self.add_attribute(EnumAttribute("dof2","sima/hydro/DOF",""))
        self.add_attribute(Attribute("values","number","",Dimension("*"),default=0.0))