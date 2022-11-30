# 
# Generated with FatigueAnalysisBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.named import NamedBlueprint

class FatigueAnalysisBlueprint(NamedBlueprint):
    """"""

    def __init__(self, name="FatigueAnalysis", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("numberOfPoints","integer","",default=8))
        self.add_attribute(Attribute("includeAllPoints","boolean","Include the results from all points in output",default=False))
        self.add_attribute(BlueprintAttribute("items","sima/riflex/FatigueAnalysisItem","Specification of nodes for displacement storage",True,Dimension("*")))
        self.add_attribute(Attribute("specifyTimeWindow","boolean","",default=False))
        self.add_attribute(Attribute("startTime","number","",default=0.0))
        self.add_attribute(Attribute("endTime","number","",default=0.0))