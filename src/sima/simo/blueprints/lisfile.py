# 
# Generated with LisFileBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.result import ResultBlueprint

class LisFileBlueprint(ResultBlueprint):
    """"""

    def __init__(self, name="LisFile", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("*")))
        self.add_attribute(Attribute("resource","string",""))
        self.add_attribute(Attribute("relative","boolean","",default=False))
        self.add_attribute(Attribute("_type","string",""))
        self.add_attribute(Attribute("time","integer","",default=-1))
        self.add_attribute(Attribute("size","integer","",default=-1))
        self.add_attribute(Attribute("runNumber","integer","",default=-1))
        self.add_attribute(BlueprintAttribute("messages","sima/sima/SimaMessage","",True,Dimension("*")))
        self.add_attribute(Attribute("runFailed","boolean","",default=False))
        self.add_attribute(Attribute("version","string",""))