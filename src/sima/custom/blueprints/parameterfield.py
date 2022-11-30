# 
# Generated with ParameterFieldBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .customcomponent import CustomComponentBlueprint
from sima.sima.blueprints.singleparameter import SingleParameterBlueprint

class ParameterFieldBlueprint(CustomComponentBlueprint,SingleParameterBlueprint):
    """"""

    def __init__(self, name="ParameterField", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))