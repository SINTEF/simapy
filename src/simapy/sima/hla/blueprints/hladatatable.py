# 
# Generated with HLADataTableBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.named import NamedBlueprint

class HLADataTableBlueprint(NamedBlueprint):
    """"""

    def __init__(self, name="HLADataTable", package_path="sima/hla", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("signals","sima/hla/HLASignal","",True,Dimension("*")))
        self.add_attribute(Attribute("showHorisontalTable","boolean","",default=False))