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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("angleZeroLift","number","Angle of attack at zero lift (Typical value: -2 deg)",default=0.0))
        self.add_attribute(Attribute("maxLinearClSlopePos","number","Max linear CL slope (positive) (Typical value: 0.12/deg)",default=0.0))
        self.add_attribute(Attribute("maxLinearClSlopeNeg","number","Max linear CL slope (negative) (Typical value: 0.12/deg)",default=0.0))
        self.add_attribute(Attribute("angleFullSeparationPos","number","Angle of attack at full separation (positive) (Typical value: 20 deg)",default=0.0))
        self.add_attribute(Attribute("angleFullSeparationNeg","number","Angle of attack at full separation (negative) (Typical value: -20 deg)",default=0.0))