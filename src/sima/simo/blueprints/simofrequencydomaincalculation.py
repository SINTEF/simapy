# 
# Generated with SIMOFrequencyDomainCalculationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SIMOFrequencyDomainCalculationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SIMOFrequencyDomainCalculation", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("analysisType","sima/simo/FrequencyAnalysisType",""))
        self.add_attribute(EnumAttribute("linearization","sima/simo/Linearization",""))
        self.add_attribute(Attribute("maximumNumberOfIterations","integer","",default=10))
        self.add_attribute(BlueprintAttribute("bodies","sima/simo/FrequencyDomainBodyItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("frequencyRangeLF","sima/simo/FrequencyRangeDefinition","",True))
        self.add_attribute(BlueprintAttribute("frequencyRangeWF","sima/simo/FrequencyRangeDefinition","",True))
        self.add_attribute(Attribute("calculateLineDynamics","boolean","",default=False))
        self.add_attribute(Attribute("estimationTime","number","",default=10800.0))
        self.add_attribute(Attribute("specifyLinesToSimulate","boolean","",default=False))
        self.add_attribute(BlueprintAttribute("linesToSimulate","sima/simo/FrequnecyDomainLineItem","",True,Dimension("*")))