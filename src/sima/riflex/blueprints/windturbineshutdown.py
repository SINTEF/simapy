# 
# Generated with WindTurbineShutdownBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WindTurbineShutdownBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WindTurbineShutdown", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("startTime","number","Start time for shutdown",default=0.0))
        self.add_attribute(BlueprintAttribute("bladePitchChangeItems","sima/riflex/BladePitchChangeItem","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("faultOption","sima/riflex/GeneratorTorqueFault",""))
        self.add_attribute(Attribute("scalingFactor","number","Scaling factor for generator torque",default=0.0))
        self.add_attribute(EnumAttribute("brakeOption","sima/riflex/MechanicalBrakeOption",""))
        self.add_attribute(Attribute("linearTorqueDampingCoefficient","number","",default=0.0))
        self.add_attribute(Attribute("timeToFullBrakeTorque","number","",default=0.0))