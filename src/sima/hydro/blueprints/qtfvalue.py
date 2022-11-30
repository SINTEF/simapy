# 
# Generated with QTFValueBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class QTFValueBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="QTFValue", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("dir1","integer","",default=0))
        self.add_attribute(Attribute("dir2","integer","",default=0))
        self.add_attribute(Attribute("freq1","integer","",default=0))
        self.add_attribute(Attribute("freq2","integer","",default=0))
        self.add_attribute(Attribute("re","number","",default=0.0))
        self.add_attribute(Attribute("im","number","",default=0.0))