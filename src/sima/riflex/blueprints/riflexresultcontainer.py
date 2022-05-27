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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("*")))
        self.attributes.append(Attribute("modelOutputFile","string","",default=""))
        self.attributes.append(Attribute("probability","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("static","sima/riflex/RIFLEXStaticResultEntry","",True))
        self.attributes.append(BlueprintAttribute("dynamic","sima/riflex/RIFLEXDynamicResultEntry","",True))
        self.attributes.append(BlueprintAttribute("eigenvalue","sima/riflex/RIFLEXEigenvalueResultEntry","",True))
        self.attributes.append(BlueprintAttribute("vivana","sima/riflex/RIFLEXVivanaResultEntry","",True))