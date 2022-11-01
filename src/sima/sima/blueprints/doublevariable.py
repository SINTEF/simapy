# 
# Generated with DoubleVariableBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .variable import VariableBlueprint

class DoubleVariableBlueprint(VariableBlueprint):
    """"""

    def __init__(self, name="DoubleVariable", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("value","number","The current value for the variable",default=0.0))
        self.attributes.append(Attribute("unit","string","unit of variable",default='-'))