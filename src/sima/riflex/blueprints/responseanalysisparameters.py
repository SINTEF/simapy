# 
# Generated with ResponseAnalysisParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ResponseAnalysisParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ResponseAnalysisParameters", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("iterationMethod","sima/riflex/ResponseIterationMethod","Response iteration method"))
        self.attributes.append(Attribute("retry","boolean","If the response iteration does not converge a second attempt will be made with the other response iteration method",default=False))
        self.attributes.append(Attribute("maxNumberOfIterations","integer","Maximum number of iterations",default=30))
        self.attributes.append(EnumAttribute("convergenceCriterion","sima/riflex/ConvergenceCriterion","Convergence criterion"))
        self.attributes.append(Attribute("convergenceLimit","number","Convergence limit for the iteration",default=0.0001))
        self.attributes.append(Attribute("initialResponseEstimate","number","Scaling factor for the initial response estimate",default=0.5))
        self.attributes.append(EnumAttribute("responseFrequencyOption","sima/riflex/ResponseFrequencyOption","Option for combining response frequencies"))
        self.attributes.append(Attribute("numberOfDominatingFrequencies","integer","Number of dominating frequencies given in user defined frequency\nranking",default=0))
        self.attributes.append(Attribute("amplitudeLimit","number","Amplitude limit for including frequency normalized by\nthe minimum diameter.",default=0.01))
        self.attributes.append(Attribute("lowerFrequencyCutoff","number","Cut-off excitation parameter ration for frequencies below the identified dominating frequency.",default=0.0))
        self.attributes.append(Attribute("upperFrequencyCutoff","number","Cut-off excitation parameter ration for frequencies above the identified dominating frequency.",default=0.0))
        self.attributes.append(Attribute("relativeStructuralDamping","number","Relative structural damping",default=0.0))
        self.attributes.append(EnumAttribute("forceSwitch","sima/riflex/ForceSwitch","Option for force calculation"))
        self.attributes.append(EnumAttribute("printSwitch","sima/riflex/PrintSwitch","Print switch"))
        self.attributes.append(Attribute("additionalStructuralDampingSpecification","boolean","This data group allows additional material and slip damping to be specified for some or all segments in the system. \nThis structural damping is read from separate files and is applied in addition to the relative structural damping level RELDAM. \nThe structural damping is given as a function of the response curvature and is therefore updated during the response iterations.",default=True))
        self.attributes.append(BlueprintAttribute("additionalStructuralDampingParameters","sima/riflex/AdditionalStructuralDampingParameters","",True,Dimension("size","")))