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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("numberOfEigenvalues","integer","Number of eigenvalues to be calculated",default=10))
        self.attributes.append(Attribute("numberOfEigenvectors","integer","Number of eigenvectors to be calculated",default=10))
        self.attributes.append(Attribute("maxRelativeError","number","Maximum acceptable relative error in computed eigenvalues",default=0.0))
        self.attributes.append(Attribute("limitValue","number","Limit value for singularity test during factorization",default=0.0))
        self.attributes.append(Attribute("orthogonalityLimit","number","Orthogonality limit",default=0.0))
        self.attributes.append(EnumAttribute("startVector","sima/riflex/EigenvalueStartVector","Start vector code"))
        self.attributes.append(Attribute("maxNumberOfIterations","integer","A positive number gives an iterative Gram-Schmidt procedure. A negative number gives a multi-pass Gram-Schmidt procedure.",default=5))
        self.attributes.append(Attribute("frequencyControlParameter","integer","Parameter controlling frequency for solving small tridiagonal eigenvalue problem",default=0))
        self.attributes.append(Attribute("shiftValue","number","Shift value",default=0.0))
        self.attributes.append(Attribute("numberOfLanczoSteps","integer","Number of Lanczos steps to be used, 0.0 result in an automatic computaion of suitable value",default=0))
        self.attributes.append(Attribute("premultiplyStartVector","boolean","Whether the start vector should be premultiplied with H or not",default=True))
        self.attributes.append(Attribute("storeVisualisationResponses","boolean","Store eigenvalue visualization file",default=True))
        self.attributes.append(Attribute("visualisationScaling","number","Scaling of eigenvectors in visual results",default=10.0))