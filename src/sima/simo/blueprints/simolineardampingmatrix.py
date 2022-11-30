# 
# Generated with SIMOLinearDampingMatrixBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.hydro.blueprints.lineardampingmatrix import LinearDampingMatrixBlueprint
from sima.sima.blueprints.named import NamedBlueprint

class SIMOLinearDampingMatrixBlueprint(LinearDampingMatrixBlueprint,NamedBlueprint):
    """"""

    def __init__(self, name="SIMOLinearDampingMatrix", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("values","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(EnumAttribute("mode","sima/simo/DampingMatrixMotionMode","Select which motions the damping matrix force should be calculated from. When 'default' is selected, low frequency motion is used for bodies of type '6 DOF - separated analysis' and total motion otherwise."))