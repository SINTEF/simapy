# 
# Generated with FoilPointBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class FoilPointBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="FoilPoint", package_path="sima/windturbine", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("x","number","Foil point in x-axis",default=0.0))
        self.add_attribute(Attribute("y","number","Foil point in y-axis",default=0.0))