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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("minForce","number","Minimum thruster force",default=0.0))
        self.add_attribute(Attribute("maxForce","number","Maximum thruster force",default=0.0))
        self.add_attribute(BlueprintAttribute("position","sima/sima/Point3","",True))
        self.add_attribute(Attribute("force","number","Resulting force, initial value if controlled by a DP-system",default=0.0))
        self.add_attribute(Attribute("forceDirection","number","Direction of thrust force in body x-y plane, initial value if controlled by a DP-system",default=0.0))
        self.add_attribute(BlueprintAttribute("thrusterDynamics","sima/simo/ThrusterDynamics","",True))
        self.add_attribute(BlueprintAttribute("controlSequence","sima/simo/ThrusterControlSequence","",True))
        self.add_attribute(BlueprintAttribute("failureSpecification","sima/simo/ThrusterFailureSpecification","",True))
        self.add_attribute(Attribute("includeSurfaceProximityLoss","boolean","Should surface proximity loss be included?",default=False))
        self.add_attribute(Attribute("includeThrusterHullInteraction","boolean","Should thruster-hull interaction be included?",default=False))
        self.add_attribute(Attribute("includeThrusterThrusterInteraction","boolean","Should thruster-thruster interaction be included?",default=False))
        self.add_attribute(Attribute("maxRps","number","The RPS giving maximum force",default=0.0))
        self.add_attribute(Attribute("diameter","number","Thruster diameter",default=0.0))
        self.add_attribute(Attribute("tunnelLength","number","Tunnel length",default=0.0))
        self.add_attribute(Attribute("baselineAngle","number","Hull angle relative to baseline (front view)",default=0.0))
        self.add_attribute(Attribute("centerlineAngle","number","Hull angle relative to centerline (top view)",default=0.0))
        self.add_attribute(Attribute("numberOfGrids","integer","Number of grids",default=0))
        self.add_attribute(Attribute("pitchRatio","number","Propeller Pitch Ratio",default=0.0))
        self.add_attribute(Attribute("bilgeRadius","number","Bilge radius",default=0.0))
        self.add_attribute(Attribute("verticalDistanceHull","number","Vertical distance from propeller center to hull",default=0.0))