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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("numVariations","integer","Number of variations",default=0))
        self.attributes.append(Attribute("maxIterations","integer","Maximum number of iterations for each variation",default=1))
        self.attributes.append(EnumAttribute("convergenceNorm","sima/riflex/ConvergenceNorm",""))
        self.attributes.append(Attribute("accuracy","number","Required accuracy measured by displacement norm",default=0.0001))
        self.attributes.append(Attribute("energyAccuracy","number","Required accuracy measured by energy norm. This value is relevant only if Convergence Norm is 'Both'.",default=0.0001))
        self.attributes.append(Attribute("offset","boolean","",default=False))
        self.attributes.append(Attribute("current","boolean","",default=False))
        self.attributes.append(Attribute("specifiedForce","boolean","",default=False))
        self.attributes.append(BlueprintAttribute("offsetVariation","sima/riflex/OffsetVariationItem","",True))
        self.attributes.append(BlueprintAttribute("currentVariation","sima/riflex/CurrentVariationItem","",True))
        self.attributes.append(BlueprintAttribute("boundaryChangeGroup","sima/riflex/BoundaryChangeGroup","",True))
        self.attributes.append(Attribute("fricActivation","boolean","Activate bottom friction forces",default=False))
        self.attributes.append(Attribute("springActivation","boolean","Activate global springs",default=False))
        self.attributes.append(Attribute("memoActivation","boolean","Activate material memory formulation (isotropic / kinematic hardening)",default=False))