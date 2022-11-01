# 
# Generated with ProplibTunnelThrusterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .ithruster import IThrusterBlueprint

class ProplibTunnelThrusterBlueprint(IThrusterBlueprint):
    """"""

    def __init__(self, name="ProplibTunnelThruster", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("minForce","number","Minimum thruster force",default=0.0))
        self.attributes.append(Attribute("maxForce","number","Maximum thruster force",default=0.0))
        self.attributes.append(BlueprintAttribute("position","sima/sima/Point3","",True))
        self.attributes.append(Attribute("force","number","Resulting force, initial value if controlled by a DP-system",default=0.0))
        self.attributes.append(Attribute("forceDirection","number","Direction of thrust force in body x-y plane, initial value if controlled by a DP-system",default=0.0))
        self.attributes.append(BlueprintAttribute("thrusterDynamics","sima/simo/ThrusterDynamics","",True))
        self.attributes.append(BlueprintAttribute("controlSequence","sima/simo/ThrusterControlSequence","",True))
        self.attributes.append(BlueprintAttribute("failureSpecification","sima/simo/ThrusterFailureSpecification","",True))
        self.attributes.append(Attribute("includeSurfaceProximityLoss","boolean","Should surface proximity loss be included?",default=True))
        self.attributes.append(Attribute("includeThrusterHullInteraction","boolean","Should thruster-hull interaction be included?",default=True))
        self.attributes.append(Attribute("includeThrusterThrusterInteraction","boolean","Should thruster-thruster interaction be included?",default=True))
        self.attributes.append(Attribute("maxRps","number","The RPS giving maximum force",default=0.0))
        self.attributes.append(Attribute("diameter","number","Thruster diameter",default=0.0))
        self.attributes.append(Attribute("tunnelLength","number","Tunnel length",default=0.0))
        self.attributes.append(Attribute("baselineAngle","number","Hull angle relative to baseline (front view)",default=0.0))
        self.attributes.append(Attribute("centerlineAngle","number","Hull angle relative to centerline (top view)",default=0.0))
        self.attributes.append(Attribute("numberOfGrids","integer","Number of grids",default=0))
        self.attributes.append(Attribute("pitchRatio","number","Propeller Pitch Ratio",default=0.0))
        self.attributes.append(Attribute("bilgeRadius","number","Bilge radius",default=0.0))
        self.attributes.append(Attribute("verticalDistanceHull","number","Vertical distance from propeller center to hull",default=0.0))