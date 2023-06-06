# 
# Generated with VariableBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .namedobject import NamedObjectBlueprint
from .singleparameter import SingleParameterBlueprint

class VariableBlueprint(NamedObjectBlueprint,SingleParameterBlueprint):
    """"""

    def __init__(self, name="Variable", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))