# 
# Generated with ReynoldItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ReynoldItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ReynoldItem", package_path="sima/windturbine", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("reynoldsNumber","number","Reynold number for given airfoil regime",default=0.0))
        self.add_attribute(BlueprintAttribute("items","sima/windturbine/AirFoilItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stallPoint","sima/windturbine/StallPoint","",True))