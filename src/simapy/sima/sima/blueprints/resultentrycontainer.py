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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("properties","sima/sima/Property","",True,Dimension("*")))
        self.add_attribute(Attribute("resource","string",""))
        self.add_attribute(Attribute("relative","boolean","",default=False))
        self.add_attribute(Attribute("changeNumber","integer","",default=0))
        self.add_attribute(BlueprintAttribute("results","sima/sima/Result","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("entries","sima/sima/ResultEntry","",True,Dimension("*")))