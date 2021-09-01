# 
# Generated with StallPointBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class StallPointBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="StallPoint", package_path="sima/windturbine", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("angleZeroLift","number","Angle of attack at zero lift (Typical value: -2 deg)",default=0.0))
        self.attributes.append(Attribute("maxLinearClSlopePos","number","Max linear CL slope (positive) (Typical value: 0.12/deg)",default=0.0))
        self.attributes.append(Attribute("maxLinearClSlopeNeg","number","Max linear CL slope (negative) (Typical value: 0.12/deg)",default=0.0))
        self.attributes.append(Attribute("angleFullSeparationPos","number","Angle of attack at full separation (positive) (Typical value: 20 deg)",default=0.0))
        self.attributes.append(Attribute("angleFullSeparationNeg","number","Angle of attack at full separation (negative) (Typical value: -20 deg)",default=0.0))