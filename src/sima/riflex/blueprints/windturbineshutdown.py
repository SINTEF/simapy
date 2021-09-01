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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("startTime","number","Start time for shutdown",default=0.0))
        self.attributes.append(BlueprintAttribute("bladePitchChangeItems","sima/riflex/BladePitchChangeItem","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("faultOption","sima/riflex/GeneratorTorqueFault",""))
        self.attributes.append(Attribute("scalingFactor","number","Scaling factor for generator torque",default=0.0))
        self.attributes.append(EnumAttribute("brakeOption","sima/riflex/MechanicalBrakeOption",""))
        self.attributes.append(Attribute("linearTorqueDampingCoefficient","number","",default=0.0))
        self.attributes.append(Attribute("timeToFullBrakeTorque","number","",default=0.0))