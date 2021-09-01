# 
# Generated with LongTermStatisticsCalculationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint
from sima.sima.blueprints.conditionselectable import ConditionSelectableBlueprint

class LongTermStatisticsCalculationBlueprint(NamedObjectBlueprint,ConditionSelectableBlueprint):
    """"""

    def __init__(self, name="LongTermStatisticsCalculation", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("relativeCompassAngle","number","Relative angle between analysis x-axis and north direction in anti-clockwise direction.\nShould match the angle given in the recieving SIMA task location.",default=0.0))
        self.attributes.append(EnumAttribute("inputReferenceSystem","sima/metocean/InputReferenceSystem","Defines the input reference system of the data.\nIf the data is defined in the Metocean system the corresponding SIMA coordinate system data is generated"))
        self.attributes.append(Attribute("applyNorsok","boolean"," Apply NORSOK N-006",default=True))
        self.attributes.append(BlueprintAttribute("longTermStatistics","sima/metocean/LongTermStatistics","",False))
        self.attributes.append(BlueprintAttribute("period","sima/metocean/LongTermStatisticsPeriod","",False))
        self.attributes.append(BlueprintAttribute("waveCalculation","sima/metocean/LongTermStatisticsWaveCalculation","",True))
        self.attributes.append(BlueprintAttribute("windCalculation","sima/metocean/LongTermStatisticsWindCalculation","",True))
        self.attributes.append(BlueprintAttribute("currentCalculation","sima/metocean/LongTermStatisticsCurrentCalculation","",True))