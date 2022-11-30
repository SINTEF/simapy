# 
# Generated with FatiguePropertiesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class FatiguePropertiesBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="FatigueProperties", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("calculationOption","sima/riflex/FatigueCalculationOption",""))
        self.add_attribute(Attribute("numCrossSectionPoints","integer","Number of points around cross-section where fatigue is",default=0))
        self.add_attribute(EnumAttribute("resultPrintOption","sima/riflex/ResultPrintOption",""))
        self.add_attribute(EnumAttribute("timeSeriesPrintOption","sima/riflex/TimeSeriesPrintOption",""))
        self.add_attribute(Attribute("timeSeriesLength","number","Length of stress time series to be generated for fatigue calculation",default=0.0))
        self.add_attribute(Attribute("timeStep","number","Time step to be used in the stress time series",default=0.0))
        self.add_attribute(Attribute("seed","integer","Seed for generating random phase angles",default=31415))
        self.add_attribute(Attribute("axialFactor","number","Default stress concentration factor for axial force contribution",default=1.0))
        self.add_attribute(Attribute("myFactor","number","Default stress concentration factor for bending about Yaxis",default=1.0))
        self.add_attribute(Attribute("mzFactor","number","Default stress concentration factor for bending about Zaxis",default=1.0))
        self.add_attribute(Attribute("crossSectionArea","number","Optional cross-section area.",default=0.0))
        self.add_attribute(Attribute("sectionModulus","number","Optional cross-section modulus.",default=0.0))
        self.add_attribute(Attribute("wallThickness","number","Optional wall thickness",default=0.0))
        self.add_attribute(BlueprintAttribute("snCurves","sima/riflex/SNCurveReference","",True,Dimension("*")))
        self.add_attribute(Attribute("includeAllSNCurves","boolean","Include all SNCurves in fatigue analysis",default=False))
        self.add_attribute(BlueprintAttribute("crossSectionReferences","sima/riflex/CrossSectionReference","",True,Dimension("*")))
        self.add_attribute(Attribute("relativeDuration","number","Relative duration / probability of the current condition",default=0.0))
        self.add_attribute(Attribute("scaledContributions","boolean","",default=False))