# 
# Generated with EigenvalueAnalysisParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class EigenvalueAnalysisParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="EigenvalueAnalysisParameters", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("numberOfEigenvalues","integer","Number of eigenvalues to be calculated",default=10))
        self.add_attribute(Attribute("maxRelativeError","number","Maximum acceptable relative error in computed eigenvalues",default=1e-10))
        self.add_attribute(Attribute("numberOfLanczoSteps","integer","Maximum number of Lanczos steps (vectors) to be used",default=0))
        self.add_attribute(Attribute("storeVisualisationResponses","boolean","Store eigenvalue visualization file",default=True))
        self.add_attribute(Attribute("visualisationScaling","number","Scaling of eigenvectors in visual results",default=10.0))
        self.add_attribute(Attribute("numberOfEigenvectors","integer","Number of eigenvectors to be printed",default=0))