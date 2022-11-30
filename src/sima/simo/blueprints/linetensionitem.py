# 
# Generated with LineTensionItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class LineTensionItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="LineTensionItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("length","number","Horizontal length of the nonlinear line",default=0.0))
        self.add_attribute(Attribute("tension","number","Horizontal tension of the nonlinear line for the given length",default=0.0))