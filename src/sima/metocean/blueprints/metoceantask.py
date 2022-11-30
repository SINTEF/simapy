# 
# Generated with MetoceanTaskBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.condition.blueprints.conditiontask import ConditionTaskBlueprint

class MetoceanTaskBlueprint(ConditionTaskBlueprint):
    """"""

    def __init__(self, name="MetoceanTask", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("doubleVariables","sima/sima/DoubleVariable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("integerVariables","sima/sima/IntegerVariable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stringVariables","sima/sima/StringVariable","",True,Dimension("*")))
        self.add_attribute(Attribute("runNumber","integer","",default=0))
        self.add_attribute(BlueprintAttribute("scripts","sima/sima/SIMAScript","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("variations","sima/condition/ModelVariation","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("referenceVariables","sima/sima/ModelReferenceVariable","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("initialCondition","sima/condition/InitialCondition","",True))
        self.add_attribute(BlueprintAttribute("conditions","sima/condition/ConditionTaskCondition","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("hindcastData","sima/metocean/HindcastData","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("scatterData","sima/metocean/ScatterData","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("longTermStatistics","sima/metocean/LongTermStatistics","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("scatterDataCalculations","sima/metocean/ScatterDataCalculation","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("hindcastDataCalculations","sima/metocean/HindcastDataCalculation","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("longTermStatisticsCalculations","sima/metocean/LongTermStatisticsCalculation","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("profiles","sima/metocean/Profile","",True,Dimension("*")))