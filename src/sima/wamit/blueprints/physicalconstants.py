# 
# Generated with PhysicalConstantsBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class PhysicalConstantsBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="PhysicalConstants", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("waterDensity","number","Water density - rho water",default=1025.0))
        self.attributes.append(Attribute("accOfGravity","number","Acceleration of gravity - g",default=9.81))