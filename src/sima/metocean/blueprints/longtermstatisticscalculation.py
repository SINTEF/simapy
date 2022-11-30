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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("relativeCompassAngle","number","Relative angle between analysis x-axis and north direction in anti-clockwise direction.\nShould match the angle given in the recieving SIMA task location.",default=0.0))
        self.add_attribute(EnumAttribute("inputReferenceSystem","sima/metocean/InputReferenceSystem","Defines the input reference system of the data.\nIf the data is defined in the Metocean system the corresponding SIMA coordinate system data is generated"))
        self.add_attribute(Attribute("applyNorsok","boolean"," Apply NORSOK N-006",default=True))
        self.add_attribute(BlueprintAttribute("longTermStatistics","sima/metocean/LongTermStatistics","",False))
        self.add_attribute(BlueprintAttribute("period","sima/metocean/LongTermStatisticsPeriod","",False))
        self.add_attribute(BlueprintAttribute("waveCalculation","sima/metocean/LongTermStatisticsWaveCalculation","",True))
        self.add_attribute(BlueprintAttribute("windCalculation","sima/metocean/LongTermStatisticsWindCalculation","",True))
        self.add_attribute(BlueprintAttribute("currentCalculation","sima/metocean/LongTermStatisticsCurrentCalculation","",True))