# 
# Generated with TimeSimulationResultBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.result import ResultBlueprint

class TimeSimulationResultBlueprint(ResultBlueprint):
    """"""

    def __init__(self, name="TimeSimulationResult", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("*")))
        self.attributes.append(Attribute("resource","string","",default=""))
        self.attributes.append(Attribute("relative","boolean","",default=False))
        self.attributes.append(Attribute("_type","string","",default=""))
        self.attributes.append(Attribute("time","integer","",default=-1))
        self.attributes.append(Attribute("size","integer","",default=-1))
        self.attributes.append(Attribute("runNumber","integer","",default=-1))
        self.attributes.append(BlueprintAttribute("messages","sima/sima/SimaMessage","",True,Dimension("*")))