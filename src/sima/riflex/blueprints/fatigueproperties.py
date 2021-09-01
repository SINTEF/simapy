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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("calculationOption","sima/riflex/FatigueCalculationOption",""))
        self.attributes.append(Attribute("numCrossSectionPoints","integer","Number of points around cross-section where fatigue is",default=0))
        self.attributes.append(EnumAttribute("resultPrintOption","sima/riflex/ResultPrintOption",""))
        self.attributes.append(EnumAttribute("timeSeriesPrintOption","sima/riflex/TimeSeriesPrintOption",""))
        self.attributes.append(Attribute("timeSeriesLength","number","Length of stress time series to be generated for fatigue calculation",default=0.0))
        self.attributes.append(Attribute("timeStep","number","Time step to be used in the stress time series",default=0.0))
        self.attributes.append(Attribute("seed","integer","Seed for generating random phase angles",default=31415))
        self.attributes.append(Attribute("axialFactor","number","Default stress concentration factor for axial force contribution",default=1.0))
        self.attributes.append(Attribute("myFactor","number","Default stress concentration factor for bending about Yaxis",default=1.0))
        self.attributes.append(Attribute("mzFactor","number","Default stress concentration factor for bending about Zaxis",default=1.0))
        self.attributes.append(Attribute("crossSectionArea","number","Optional cross-section area.",default=0.0))
        self.attributes.append(Attribute("sectionModulus","number","Optional cross-section modulus.",default=0.0))
        self.attributes.append(Attribute("wallThickness","number","Optional wall thickness",default=0.0))
        self.attributes.append(BlueprintAttribute("snCurves","sima/riflex/SNCurveReference","",True,Dimension("size","")))
        self.attributes.append(Attribute("includeAllSNCurves","boolean","Include all SNCurves in fatigue analysis",default=False))
        self.attributes.append(BlueprintAttribute("crossSectionReferences","sima/riflex/CrossSectionReference","",True,Dimension("size","")))
        self.attributes.append(Attribute("relativeDuration","number","Relative duration / probability of the current condition",default=0.0))
        self.attributes.append(Attribute("scaledContributions","boolean","",default=False))