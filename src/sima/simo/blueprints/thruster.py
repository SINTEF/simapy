# 
# Generated with ThrusterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .ithruster import IThrusterBlueprint

class ThrusterBlueprint(IThrusterBlueprint):
    """"""

    def __init__(self, name="Thruster", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("minForce","number","Minimum thruster force",default=0.0))
        self.add_attribute(Attribute("maxForce","number","Maximum thruster force",default=0.0))
        self.add_attribute(EnumAttribute("_type","sima/simo/ThrusterType","Thruster type"))
        self.add_attribute(BlueprintAttribute("attachmentPoint","sima/sima/Point3","",True))
        self.add_attribute(Attribute("diameter","number","Thruster diameter",default=1.0))
        self.add_attribute(Attribute("forceDirection","number","Direction of thrust force in body x-y plane, initial value if controlled by a DP-system",default=0.0))
        self.add_attribute(Attribute("force","number","Resulting force, initial value if controlled by a DP-system",default=0.0))
        self.add_attribute(Attribute("minTimeChange","number","Minimum time to change from 10% to 90% of maximum thrust",default=0.0))
        self.add_attribute(Attribute("maxRevolvingSpeed","number","Maximum revolving speed of rotatable thrusters",default=10.0))
        self.add_attribute(EnumAttribute("failureMode","sima/simo/ThrusterFailureMode","Thruster failure mode"))
        self.add_attribute(Attribute("failureTime","number","Time for thruster failure",default=0.0))
        self.add_attribute(Attribute("maxRudderAngle","number","Maximum rudder angle",default=0.0))
        self.add_attribute(Attribute("rudderCoefficient","number","Rudder coefficient",default=0.0))
        self.add_attribute(BlueprintAttribute("reductionItems","sima/simo/ThrusterReduction","",True,Dimension("*")))
        self.add_attribute(Attribute("relativeDeadBand","number","Relative dead band, minimum change of force relative to total change",default=0.01))
        self.add_attribute(Attribute("thrustReductionFactor","number","Thrust reduction factor",default=1.0))
        self.add_attribute(Attribute("minDirectionChange","number","Minimum change in direction of thrusters force",default=0.0))
        self.add_attribute(BlueprintAttribute("forbiddenZoneItems","sima/simo/ThrusterForbiddenZone","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("formulation","sima/simo/Formulation",""))
        self.add_attribute(Attribute("ctForward","number","Modification factor for forward thrust",default=1.0))
        self.add_attribute(Attribute("cqForward","number","Modification factor for forward torque",default=1.0))
        self.add_attribute(Attribute("ctReverse","number","Modification factor for reverse thrust",default=1.0))
        self.add_attribute(Attribute("cqReverse","number","Modification factor for reverse torque",default=1.0))
        self.add_attribute(Attribute("pdRatio","number","Pitch-diameter ratio",default=1.0))
        self.add_attribute(Attribute("tcThrust","number","Time constant of thrust",default=0.0))
        self.add_attribute(Attribute("tcAzimuth","number","Time constant of azimuth change",default=0.0))
        self.add_attribute(EnumAttribute("coefficientModel","sima/simo/ThrustCoefficientModel",""))
        self.add_attribute(BlueprintAttribute("forwardThrustTorqueCoefficients","sima/simo/ThrustTorqueCoefficient","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("reverseThrustTorqueCoefficients","sima/simo/ThrustTorqueCoefficient","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("thrustLoss","sima/simo/ThrustLoss",""))
        self.add_attribute(BlueprintAttribute("surfaceProximityReductionFactors","sima/simo/SurfaceProximityReductionFactor","",True,Dimension("*")))
        self.add_attribute(Attribute("specifyControlSequence","boolean","Should a list of control signals be specified for thruster?",default=False))
        self.add_attribute(EnumAttribute("controlSequenceSignalType","sima/simo/ThrustSignalType","Unit for demanded thrust force"))
        self.add_attribute(BlueprintAttribute("controlSequence","sima/simo/ControlSequenceItem","",True,Dimension("*")))