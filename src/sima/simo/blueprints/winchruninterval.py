# 
# Generated with WinchRunIntervalBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WinchRunIntervalBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WinchRunInterval", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("startTime","number","Start time for running winch",default=0.0))
        self.attributes.append(Attribute("stopTime","number","Stop time for running winch",default=0.0))
        self.attributes.append(Attribute("speed","number","Winch run velocity (positive when paying out)",default=0.0))