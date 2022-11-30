# 
# Generated with WamitWaveDriftForceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.hydro.blueprints.wavedriftforce import WaveDriftForceBlueprint
from sima.sima.blueprints.named import NamedBlueprint

class WamitWaveDriftForceBlueprint(WaveDriftForceBlueprint,NamedBlueprint):
    """"""

    def __init__(self, name="WamitWaveDriftForce", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("directions","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("frequencies","number","",Dimension("*"),default=0.0))
        self.add_attribute(EnumAttribute("symmetry","sima/hydro/DirectionSymmetry",""))
        self.add_attribute(BlueprintAttribute("fx","sima/hydro/DirectionDependentValues","",True))
        self.add_attribute(BlueprintAttribute("fy","sima/hydro/DirectionDependentValues","",True))
        self.add_attribute(BlueprintAttribute("fz","sima/hydro/DirectionDependentValues","",True))
        self.add_attribute(BlueprintAttribute("mx","sima/hydro/DirectionDependentValues","",True))
        self.add_attribute(BlueprintAttribute("my","sima/hydro/DirectionDependentValues","",True))
        self.add_attribute(BlueprintAttribute("mz","sima/hydro/DirectionDependentValues","",True))
        self.add_attribute(Attribute("name","string",""))