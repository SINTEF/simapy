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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("doubleVariables","sima/sima/DoubleVariable","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("integerVariables","sima/sima/IntegerVariable","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("stringVariables","sima/sima/StringVariable","",True,Dimension("size","")))
        self.attributes.append(Attribute("runNumber","integer","",default=0))
        self.attributes.append(BlueprintAttribute("scripts","sima/sima/SIMAScript","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("variations","sima/condition/ModelVariation","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("referenceVariables","sima/condition/ModelReferenceVariable","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("initialCondition","sima/condition/InitialCondition","",True))
        self.attributes.append(BlueprintAttribute("conditions","sima/condition/ConditionTaskCondition","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("hindcastData","sima/metocean/HindcastData","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("scatterData","sima/metocean/ScatterData","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("longTermStatistics","sima/metocean/LongTermStatistics","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("scatterDataCalculations","sima/metocean/ScatterDataCalculation","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("hindcastDataCalculations","sima/metocean/HindcastDataCalculation","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("longTermStatisticsCalculations","sima/metocean/LongTermStatisticsCalculation","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("profiles","sima/metocean/Profile","",True,Dimension("size","")))