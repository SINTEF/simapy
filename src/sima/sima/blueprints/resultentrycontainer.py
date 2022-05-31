# 
# Generated with ResultEntryContainerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .resultcontainer import ResultContainerBlueprint
from .resultentry import ResultEntryBlueprint

class ResultEntryContainerBlueprint(ResultContainerBlueprint,ResultEntryBlueprint):
    """"""

    def __init__(self, name="ResultEntryContainer", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("*")))
        self.attributes.append(Attribute("resource","string","",default=""))
        self.attributes.append(Attribute("relative","boolean","",default=False))
        self.attributes.append(Attribute("changeNumber","integer","",default=0))
        self.attributes.append(BlueprintAttribute("results","sima/sima/Result","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("entries","sima/sima/ResultEntry","",True,Dimension("*")))