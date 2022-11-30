# 
# Generated with WindRotorSpeedItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WindRotorSpeedItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WindRotorSpeedItem", package_path="sima/windturbine", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("windSpeed","number","Wind speed at hub",default=0.0))
        self.add_attribute(Attribute("rotorSpeed","number","Rotor speed",default=0.0))