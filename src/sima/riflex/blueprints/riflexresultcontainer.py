# 
# Generated with RIFLEXResultContainerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.conditionresultcontainer import ConditionResultContainerBlueprint

class RIFLEXResultContainerBlueprint(ConditionResultContainerBlueprint):
    """"""

    def __init__(self, name="RIFLEXResultContainer", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("*")))
        self.add_attribute(Attribute("modelOutputFile","string",""))
        self.add_attribute(Attribute("probability","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("static","sima/riflex/RIFLEXStaticResultEntry","",True))
        self.add_attribute(BlueprintAttribute("dynamic","sima/riflex/RIFLEXDynamicResultEntry","",True))
        self.add_attribute(BlueprintAttribute("eigenvalue","sima/riflex/RIFLEXEigenvalueResultEntry","",True))
        self.add_attribute(BlueprintAttribute("vivana","sima/riflex/RIFLEXVivanaResultEntry","",True))