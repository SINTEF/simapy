# 
# Generated with SIMOQuadraticDampingMatrixBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.hydro.blueprints.quadraticdampingmatrix import QuadraticDampingMatrixBlueprint

class SIMOQuadraticDampingMatrixBlueprint(QuadraticDampingMatrixBlueprint):
    """"""

    def __init__(self, name="SIMOQuadraticDampingMatrix", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("values","number","",Dimension("size",""),default=0.0))
        self.attributes.append(EnumAttribute("mode","sima/simo/DampingMatrixMotionMode","Select which motions the damping matrix force should be calculated from. When 'default' is selected, low frequency motion is used for bodies of type '6 DOF - separated analysis' and total motion otherwise."))