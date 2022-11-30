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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("_type","sima/simo/ArticulatedStructureType","Type of articulated structure coupling control"))
        self.add_attribute(BlueprintAttribute("masterPoint","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("localPoint","sima/sima/Point3","",True))
        self.add_attribute(EnumAttribute("motionMode","sima/simo/MotionMode","Mode of motion (X,Y,Z,PHI,THETA,PSI)"))
        self.add_attribute(Attribute("initialPosition","number","Initial position",default=0.0))
        self.add_attribute(Attribute("lowerPositionLimit","number","Lower position limit in master coordinate system",default=0.0))
        self.add_attribute(Attribute("upperPositionLimit","number","Upper position limit in master coordinate system",default=0.0))
        self.add_attribute(Attribute("maxSpeed","number","Maximum speed for chosen mode of motion",default=0.0))
        self.add_attribute(Attribute("maxAcceleration","number","Maximum acceleration for chosen mode of motion",default=0.0))
        self.add_attribute(BlueprintAttribute("sequenceItems","sima/simo/MotionSequence","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("motionSequenceType","sima/simo/MotionSequenceType",""))
        self.add_attribute(Attribute("maximumAngle","number","Maximum angle that turret follows the vessel before sliding",default=0.0))
        self.add_attribute(Attribute("slipAngle","number","Slip (turn-back) angle",default=0.0))