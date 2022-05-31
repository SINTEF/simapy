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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("analysisType","sima/simo/FrequencyAnalysisType",""))
        self.attributes.append(EnumAttribute("linearization","sima/simo/Linearization",""))
        self.attributes.append(Attribute("maximumNumberOfIterations","integer","",default=10))
        self.attributes.append(BlueprintAttribute("bodies","sima/simo/FrequencyDomainBodyItem","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("frequencyRangeLF","sima/simo/FrequencyRangeDefinition","",True))
        self.attributes.append(BlueprintAttribute("frequencyRangeWF","sima/simo/FrequencyRangeDefinition","",True))
        self.attributes.append(Attribute("calculateLineDynamics","boolean","",default=True))
        self.attributes.append(Attribute("estimationTime","number","",default=10800.0))
        self.attributes.append(Attribute("specifyLinesToSimulate","boolean","",default=True))
        self.attributes.append(BlueprintAttribute("linesToSimulate","sima/simo/FrequnecyDomainLineItem","",True,Dimension("*")))