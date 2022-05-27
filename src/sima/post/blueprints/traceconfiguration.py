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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("path","string","",default=""))
        self.attributes.append(Attribute("label","string","",default=""))
        self.attributes.append(BlueprintAttribute("color","sima/sima/SIMAColor","",True))
        self.attributes.append(EnumAttribute("lineStyle","sima/post/LineStyle",""))
        self.attributes.append(Attribute("lineWidth","integer","",default=1))
        self.attributes.append(EnumAttribute("pointStyle","sima/post/PointStyle",""))
        self.attributes.append(Attribute("showStatistics","boolean","",default=True))
        self.attributes.append(Attribute("pointSize","integer","",default=1))
        self.attributes.append(Attribute("specifyPath","boolean","",default=False))