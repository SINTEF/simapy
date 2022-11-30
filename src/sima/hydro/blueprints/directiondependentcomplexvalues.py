# 
# Generated with DirectionDependentComplexValuesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DirectionDependentComplexValuesBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DirectionDependentComplexValues", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("directionalValues","sima/hydro/ComplexValues","",True,Dimension("*")))