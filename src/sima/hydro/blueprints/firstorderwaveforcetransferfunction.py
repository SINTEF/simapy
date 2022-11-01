# 
# Generated with FirstOrderWaveForceTransferFunctionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class FirstOrderWaveForceTransferFunctionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="FirstOrderWaveForceTransferFunction", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("directions","number","",Dimension("*"),default=0.0))
        self.attributes.append(Attribute("frequencies","number","",Dimension("*"),default=0.0))
        self.attributes.append(EnumAttribute("symmetry","sima/hydro/DirectionSymmetry",""))
        self.attributes.append(BlueprintAttribute("fx","sima/hydro/DirectionDependentComplexValues","",True))
        self.attributes.append(BlueprintAttribute("fy","sima/hydro/DirectionDependentComplexValues","",True))
        self.attributes.append(BlueprintAttribute("fz","sima/hydro/DirectionDependentComplexValues","",True))
        self.attributes.append(BlueprintAttribute("mx","sima/hydro/DirectionDependentComplexValues","",True))
        self.attributes.append(BlueprintAttribute("my","sima/hydro/DirectionDependentComplexValues","",True))
        self.attributes.append(BlueprintAttribute("mz","sima/hydro/DirectionDependentComplexValues","",True))