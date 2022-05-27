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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("include","boolean","",default=False))
        self.attributes.append(EnumAttribute("eventType","sima/riflex/IEC2005WindEventType",""))
        self.attributes.append(Attribute("eventStartTime","number","Time for event to start",default=0.0))
        self.attributes.append(EnumAttribute("direction","sima/riflex/WindDirection",""))
        self.attributes.append(EnumAttribute("turbineClass","sima/riflex/IEC2005WindTurbineClass",""))
        self.attributes.append(Attribute("vref","number","Reference wind speed average over 10 minutes",default=0.0))
        self.attributes.append(Attribute("iref","number","Expected value of the turbulence intensity at 15 m/s",default=0.0))
        self.attributes.append(Attribute("velocityChange","number","",default=0.0))
        self.attributes.append(Attribute("directionChange","number","",default=0.0))
        self.attributes.append(Attribute("durationOfEvent","number","",default=0.0))
        self.attributes.append(Attribute("gustMagnitude","number","",default=0.0))