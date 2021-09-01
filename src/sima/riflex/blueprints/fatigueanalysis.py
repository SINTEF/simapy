# 
# Generated with FatigueAnalysisBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class FatigueAnalysisBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="FatigueAnalysis", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("numberOfPoints","integer","",default=8))
        self.attributes.append(Attribute("includeAllPoints","boolean","Include the results from all points in output",default=False))
        self.attributes.append(BlueprintAttribute("items","sima/riflex/FatigueAnalysisItem","Specification of nodes for displacement storage",True,Dimension("size","")))
        self.attributes.append(Attribute("specifyTimeWindow","boolean","",default=False))
        self.attributes.append(Attribute("startTime","number","",default=0.0))
        self.attributes.append(Attribute("endTime","number","",default=0.0))