# 
# Generated with ScriptableValueBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class ScriptableValueBlueprint(Blueprint):
    """"""

    def __init__(self, name="ScriptableValue", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(Attribute("script","string","",default=""))
        self.attributes.append(BlueprintAttribute("dependencies","sima/sima/Dependency","",True,Dimension("*")))
        self.attributes.append(Attribute("cyclic","boolean","",default=False))
        self.attributes.append(Attribute("feature","string","",default=""))
        self.attributes.append(Attribute("index","integer","",default=-1))