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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("minForce","number","Minimum thruster force",default=0.0))
        self.attributes.append(Attribute("maxForce","number","Maximum thruster force",default=0.0))
        self.attributes.append(EnumAttribute("_type","sima/simo/ThrusterType","Thruster type"))
        self.attributes.append(BlueprintAttribute("attachmentPoint","sima/sima/Point3","",True))
        self.attributes.append(Attribute("diameter","number","Thruster diameter",default=1.0))
        self.attributes.append(Attribute("forceDirection","number","Direction of thrust force in body x-y plane, initial value if controlled by a DP-system",default=0.0))
        self.attributes.append(Attribute("force","number","Resulting force, initial value if controlled by a DP-system",default=0.0))
        self.attributes.append(Attribute("minTimeChange","number","Minimum time to change from 10% to 90% of maximum thrust",default=0.0))
        self.attributes.append(Attribute("maxRevolvingSpeed","number","Maximum revolving speed of rotatable thrusters",default=10.0))
        self.attributes.append(EnumAttribute("failureMode","sima/simo/ThrusterFailureMode","Thruster failure mode"))
        self.attributes.append(Attribute("failureTime","number","Time for thruster failure",default=0.0))
        self.attributes.append(Attribute("maxRudderAngle","number","Maximum rudder angle",default=0.0))
        self.attributes.append(Attribute("rudderCoefficient","number","Rudder coefficient",default=0.0))
        self.attributes.append(BlueprintAttribute("reductionItems","sima/simo/ThrusterReduction","",True,Dimension("*")))
        self.attributes.append(Attribute("relativeDeadBand","number","Relative dead band, minimum change of force relative to total change",default=0.01))
        self.attributes.append(Attribute("thrustReductionFactor","number","Thrust reduction factor",default=1.0))
        self.attributes.append(Attribute("minDirectionChange","number","Minimum change in direction of thrusters force",default=0.0))
        self.attributes.append(BlueprintAttribute("forbiddenZoneItems","sima/simo/ThrusterForbiddenZone","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("formulation","sima/simo/Formulation",""))
        self.attributes.append(Attribute("ctForward","number","Modification factor for forward thrust",default=1.0))
        self.attributes.append(Attribute("cqForward","number","Modification factor for forward torque",default=1.0))
        self.attributes.append(Attribute("ctReverse","number","Modification factor for reverse thrust",default=1.0))
        self.attributes.append(Attribute("cqReverse","number","Modification factor for reverse torque",default=1.0))
        self.attributes.append(Attribute("pdRatio","number","Pitch-diameter ratio",default=1.0))
        self.attributes.append(Attribute("tcThrust","number","Time constant of thrust",default=0.0))
        self.attributes.append(Attribute("tcAzimuth","number","Time constant of azimuth change",default=0.0))
        self.attributes.append(EnumAttribute("coefficientModel","sima/simo/ThrustCoefficientModel",""))
        self.attributes.append(BlueprintAttribute("forwardThrustTorqueCoefficients","sima/simo/ThrustTorqueCoefficient","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("reverseThrustTorqueCoefficients","sima/simo/ThrustTorqueCoefficient","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("thrustLoss","sima/simo/ThrustLoss",""))
        self.attributes.append(BlueprintAttribute("surfaceProximityReductionFactors","sima/simo/SurfaceProximityReductionFactor","",True,Dimension("*")))
        self.attributes.append(Attribute("specifyControlSequence","boolean","Should a list of control signals be specified for thruster?",default=False))
        self.attributes.append(EnumAttribute("controlSequenceSignalType","sima/simo/ThrustSignalType","Unit for demanded thrust force"))
        self.attributes.append(BlueprintAttribute("controlSequence","sima/simo/ControlSequenceItem","",True,Dimension("*")))