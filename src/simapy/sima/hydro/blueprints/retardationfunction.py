# 
# Generated with RetardationFunctionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class RetardationFunctionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RetardationFunction", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("retardationElements","sima/hydro/RetardationElementData","",True,Dimension("*")))
        self.add_attribute(Attribute("timeDelay","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("additionalDamping","sima/hydro/LinearDampingMatrix","",True))