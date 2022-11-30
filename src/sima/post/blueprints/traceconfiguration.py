# 
# Generated with TraceConfigurationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .pathspecification import PathSpecificationBlueprint

class TraceConfigurationBlueprint(PathSpecificationBlueprint):
    """"""

    def __init__(self, name="TraceConfiguration", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("path","string",""))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("label","string",""))
        self.add_attribute(BlueprintAttribute("color","sima/sima/SIMAColor","",True))
        self.add_attribute(EnumAttribute("lineStyle","sima/post/LineStyle",""))
        self.add_attribute(Attribute("lineWidth","integer","",default=1))
        self.add_attribute(EnumAttribute("pointStyle","sima/post/PointStyle",""))
        self.add_attribute(Attribute("showStatistics","boolean","",default=True))
        self.add_attribute(Attribute("pointSize","integer","",default=1))
        self.add_attribute(Attribute("specifyPath","boolean","",default=False))