# 
# Generated with WaveDriftForceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WaveDriftForceBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WaveDriftForce", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("directions","number","",Dimension("size",""),default=0.0))
        self.attributes.append(Attribute("frequencies","number","",Dimension("size",""),default=0.0))
        self.attributes.append(EnumAttribute("symmetry","sima/hydro/DirectionSymmetry",""))
        self.attributes.append(BlueprintAttribute("fx","sima/hydro/DirectionDependentValues","",True))
        self.attributes.append(BlueprintAttribute("fy","sima/hydro/DirectionDependentValues","",True))
        self.attributes.append(BlueprintAttribute("fz","sima/hydro/DirectionDependentValues","",True))
        self.attributes.append(BlueprintAttribute("mx","sima/hydro/DirectionDependentValues","",True))
        self.attributes.append(BlueprintAttribute("my","sima/hydro/DirectionDependentValues","",True))
        self.attributes.append(BlueprintAttribute("mz","sima/hydro/DirectionDependentValues","",True))