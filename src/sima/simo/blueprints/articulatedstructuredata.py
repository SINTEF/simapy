# 
# Generated with ArticulatedStructureDataBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ArticulatedStructureDataBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ArticulatedStructureData", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("_type","sima/simo/ArticulatedStructureType","Type of articulated structure coupling control"))
        self.attributes.append(BlueprintAttribute("masterPoint","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("localPoint","sima/sima/Point3","",True))
        self.attributes.append(EnumAttribute("motionMode","sima/simo/MotionMode","Mode of motion (X,Y,Z,PHI,THETA,PSI)"))
        self.attributes.append(Attribute("initialPosition","number","Initial position",default=0.0))
        self.attributes.append(Attribute("lowerPositionLimit","number","Lower position limit in master coordinate system",default=0.0))
        self.attributes.append(Attribute("upperPositionLimit","number","Upper position limit in master coordinate system",default=0.0))
        self.attributes.append(Attribute("maxSpeed","number","Maximum speed for chosen mode of motion",default=0.0))
        self.attributes.append(Attribute("maxAcceleration","number","Maximum acceleration for chosen mode of motion",default=0.0))
        self.attributes.append(BlueprintAttribute("sequenceItems","sima/simo/MotionSequence","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("motionSequenceType","sima/simo/MotionSequenceType",""))
        self.attributes.append(Attribute("maximumAngle","number","Maximum angle that turret follows the vessel before sliding",default=0.0))
        self.attributes.append(Attribute("slipAngle","number","Slip (turn-back) angle",default=0.0))