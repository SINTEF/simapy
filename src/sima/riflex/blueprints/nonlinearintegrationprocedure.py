# 
# Generated with NonLinearIntegrationProcedureBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class NonLinearIntegrationProcedureBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="NonLinearIntegrationProcedure", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("equilibriumIterationFrequency","integer","Frequency of equilibrium iteration",default=1))
        self.attributes.append(EnumAttribute("iterationType","sima/riflex/IterationType","Type of iteration if iteration is to be performed"))
        self.attributes.append(Attribute("maxIterations","integer","Maximum number of iterations for steps with iteration",default=10))
        self.attributes.append(EnumAttribute("convergenceNorm","sima/riflex/ConvergenceNorm",""))
        self.attributes.append(Attribute("equilibriumIterationAccuracy","number","Desired accuracy for equilibrium iteration measured by a modified euclidian displacement norm (norm of squared translations). Recommended values: 10e-6 - 10e-5.",default=1e-05))
        self.attributes.append(Attribute("energyAccuracy","number","Required accuracy measured by energy norm. This value is relevant only if Convergence Norm is 'Both'.",default=1e-05))
        self.attributes.append(EnumAttribute("iterationContinuation","sima/riflex/IterationContinuationCode","Code for continuation after iteration"))
        self.attributes.append(Attribute("autoTimeStepSubdivision","integer","Code for automatic subdivision of time step",default=0))
        self.attributes.append(Attribute("timeIntegrationInfo","integer","Code for time integration information",default=1))