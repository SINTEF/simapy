# 
# Generated with FirstOrderMotionTransferFunctionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class FirstOrderMotionTransferFunctionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="FirstOrderMotionTransferFunction", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("directions","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("frequencies","number","",Dimension("*"),default=0.0))
        self.add_attribute(EnumAttribute("symmetry","sima/hydro/DirectionSymmetry",""))
        self.add_attribute(Attribute("hfReference","number","Transfer function reference position",default=0.0))
        self.add_attribute(BlueprintAttribute("surge","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(BlueprintAttribute("sway","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(BlueprintAttribute("heave","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(BlueprintAttribute("roll","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(BlueprintAttribute("pitch","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(BlueprintAttribute("yaw","sima/hydro/DirectionDependentComplexValues","",True))