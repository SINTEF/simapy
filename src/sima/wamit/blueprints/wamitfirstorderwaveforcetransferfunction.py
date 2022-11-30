# 
# Generated with WamitFirstOrderWaveForceTransferFunctionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.hydro.blueprints.firstorderwaveforcetransferfunction import FirstOrderWaveForceTransferFunctionBlueprint
from sima.sima.blueprints.named import NamedBlueprint

class WamitFirstOrderWaveForceTransferFunctionBlueprint(FirstOrderWaveForceTransferFunctionBlueprint,NamedBlueprint):
    """"""

    def __init__(self, name="WamitFirstOrderWaveForceTransferFunction", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("directions","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("frequencies","number","",Dimension("*"),default=0.0))
        self.add_attribute(EnumAttribute("symmetry","sima/hydro/DirectionSymmetry",""))
        self.add_attribute(BlueprintAttribute("fx","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(BlueprintAttribute("fy","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(BlueprintAttribute("fz","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(BlueprintAttribute("mx","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(BlueprintAttribute("my","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(BlueprintAttribute("mz","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(Attribute("name","string",""))