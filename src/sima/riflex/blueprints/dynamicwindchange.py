# 
# Generated with DynamicWindChangeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DynamicWindChangeBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DynamicWindChange", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("include","boolean","",default=False))
        self.add_attribute(EnumAttribute("eventType","sima/riflex/IEC2005WindEventType",""))
        self.add_attribute(Attribute("eventStartTime","number","Time for event to start",default=0.0))
        self.add_attribute(EnumAttribute("direction","sima/riflex/WindDirection",""))
        self.add_attribute(EnumAttribute("turbineClass","sima/riflex/IEC2005WindTurbineClass",""))
        self.add_attribute(Attribute("vref","number","Reference wind speed average over 10 minutes",default=0.0))
        self.add_attribute(Attribute("iref","number","Expected value of the turbulence intensity at 15 m/s",default=0.0))
        self.add_attribute(Attribute("velocityChange","number","",default=0.0))
        self.add_attribute(Attribute("directionChange","number","",default=0.0))
        self.add_attribute(Attribute("durationOfEvent","number","",default=0.0))
        self.add_attribute(Attribute("gustMagnitude","number","",default=0.0))