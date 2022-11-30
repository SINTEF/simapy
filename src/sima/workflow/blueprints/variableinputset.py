# 
# Generated with VariableInputSetBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class VariableInputSetBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="VariableInputSet", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("parameter","sima/sima/SingleParameter","",False))
        self.add_attribute(Attribute("variations","string","",Dimension("*")))