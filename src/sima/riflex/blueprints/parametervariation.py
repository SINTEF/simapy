# 
# Generated with ParameterVariationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ParameterVariationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ParameterVariation", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("numVariations","integer","Number of variations",default=0))
        self.add_attribute(Attribute("maxIterations","integer","Maximum number of iterations for each variation",default=1))
        self.add_attribute(EnumAttribute("convergenceNorm","sima/riflex/ConvergenceNorm",""))
        self.add_attribute(Attribute("accuracy","number","Required accuracy measured by displacement norm",default=0.0001))
        self.add_attribute(Attribute("energyAccuracy","number","Required accuracy measured by energy norm. This value is relevant only if Convergence Norm is 'Both'.",default=0.0001))
        self.add_attribute(Attribute("offset","boolean","",default=False))
        self.add_attribute(Attribute("current","boolean","",default=False))
        self.add_attribute(Attribute("specifiedForce","boolean","",default=False))
        self.add_attribute(BlueprintAttribute("offsetVariation","sima/riflex/OffsetVariationItem","",True))
        self.add_attribute(BlueprintAttribute("currentVariation","sima/riflex/CurrentVariationItem","",True))
        self.add_attribute(BlueprintAttribute("boundaryChangeGroup","sima/riflex/BoundaryChangeGroup","",True))
        self.add_attribute(Attribute("fricActivation","boolean","Activate bottom friction forces",default=False))
        self.add_attribute(Attribute("springActivation","boolean","Activate global springs",default=False))
        self.add_attribute(Attribute("memoActivation","boolean","Activate material memory formulation (isotropic / kinematic hardening)",default=False))