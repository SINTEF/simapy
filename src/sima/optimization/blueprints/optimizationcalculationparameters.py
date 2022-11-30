# 
# Generated with OptimizationCalculationParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class OptimizationCalculationParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="OptimizationCalculationParameters", package_path="sima/optimization", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("desiredFinalAccuracy","number","Desired final accuracy. Should not be much smaller than the accuracy by which the gradients are computed.",default=0.01))
        self.add_attribute(Attribute("tolerance","number","Tolerance needed for the QP solver to perform several tests, for example whether optimality conditions are satisfied or whether a  number is considered as zero or not.",default=1e-12))
        self.add_attribute(Attribute("minStepLength","number","Minimum step length in case there is more than one parallel system. Recommended is any value in the order of the accuracy by which the functions are computed.",default=1e-12))
        self.add_attribute(Attribute("maxFunctionCalls","integer","Maximum number of function calls during line search. Should not be larger than 50.",default=20))
        self.add_attribute(Attribute("maxIterations","integer","Maximum number of outer iterations, where one iteration corresponds to one formulation and solution of the quadratic programming subproblem, or, alternatively one evaluation of the gradients.",default=20))
        self.add_attribute(Attribute("stackSize","integer","Stack size for storing merit function values at previous iterations for non-monotone line search. If set to zero, monotone line search is performed. Should not be greater than 50.",default=10))
        self.add_attribute(Attribute("automaticNormalization","boolean","Automatic normalization of optimization problem",default=True))
        self.add_attribute(Attribute("handleFailure","boolean","Try another solution if the underlying calculation fails",default=True))