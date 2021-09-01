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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("reynoldsNumber","number","Reynold number for given airfoil regime",default=0.0))
        self.attributes.append(BlueprintAttribute("items","sima/windturbine/AirFoilItem","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("stallPoint","sima/windturbine/StallPoint","",True))