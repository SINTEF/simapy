# 
# Generated with NonLinearForceModelBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class NonLinearForceModelBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="NonLinearForceModel", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("internalSlugFlow","boolean","Indicator for modelling forces from internal slug flow",default=False))
        self.attributes.append(EnumAttribute("hydrodynamicForce","sima/riflex/HydrodynamicForceIndicator","Indicator for hydrodynamic force model"))
        self.attributes.append(Attribute("maxHit","integer","Maximum number of load iterations (linear analysis). A negative value gives print of convergence for each step.",default=5))
        self.attributes.append(Attribute("forceIterationConvergence","number","Convergence control parameter for force iteration",default=0.01))
        self.attributes.append(Attribute("startUpDuration","number","Duration of start-up procedure",default=10.0))
        self.attributes.append(Attribute("ruptureRelease","boolean","Indicator for rupture / release",default=False))
        self.attributes.append(Attribute("connectorNumber","integer","Global ball-joint connector ID in the RIFLEX FEM model",default=0))
        self.attributes.append(Attribute("timeStepNumForRelease","integer","Time step number for release (nonlinear analysis only). In linear analysis the connector will be released at the first step.",default=0))
        self.attributes.append(EnumAttribute("dampingMatrixCalculation","sima/riflex/DampingMatrixCalculationOption","Option for calculation of proportional damping matrix in nonlinear analysis. Irrelevant for linear analysis."))
        self.attributes.append(BlueprintAttribute("slugForceSpecification","sima/riflex/SlugForceSpecification","",True))