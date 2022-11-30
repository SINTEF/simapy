# 
# Generated with EigenvalueAnalysisParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class EigenvalueAnalysisParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="EigenvalueAnalysisParameters", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("numberOfEigenvalues","integer","Number of eigenvalues to be calculated",default=10))
        self.add_attribute(Attribute("numberOfEigenvectors","integer","Number of eigenvectors to be calculated",default=10))
        self.add_attribute(Attribute("maxRelativeError","number","Maximum acceptable relative error in computed eigenvalues",default=0.0))
        self.add_attribute(Attribute("limitValue","number","Limit value for singularity test during factorization",default=0.0))
        self.add_attribute(Attribute("orthogonalityLimit","number","Orthogonality limit",default=0.0))
        self.add_attribute(EnumAttribute("startVector","sima/riflex/EigenvalueStartVector","Start vector code"))
        self.add_attribute(Attribute("maxNumberOfIterations","integer","A positive number gives an iterative Gram-Schmidt procedure. A negative number gives a multi-pass Gram-Schmidt procedure.",default=5))
        self.add_attribute(Attribute("frequencyControlParameter","integer","Parameter controlling frequency for solving small tridiagonal eigenvalue problem",default=0))
        self.add_attribute(Attribute("shiftValue","number","Shift value",default=0.0))
        self.add_attribute(Attribute("numberOfLanczoSteps","integer","Number of Lanczos steps to be used, 0.0 result in an automatic computaion of suitable value",default=0))
        self.add_attribute(Attribute("premultiplyStartVector","boolean","Whether the start vector should be premultiplied with H or not",default=True))
        self.add_attribute(Attribute("storeVisualisationResponses","boolean","Store eigenvalue visualization file",default=True))
        self.add_attribute(Attribute("visualisationScaling","number","Scaling of eigenvectors in visual results",default=10.0))