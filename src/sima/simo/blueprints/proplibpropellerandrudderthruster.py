# 
# Generated with ProplibPropellerAndRudderThrusterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .ithruster import IThrusterBlueprint

class ProplibPropellerAndRudderThrusterBlueprint(IThrusterBlueprint):
    """"""

    def __init__(self, name="ProplibPropellerAndRudderThruster", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
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
        self.attributes.append(Attribute("bladeAreaRatio","number","Propeller blade area ratio",default=0.0))
        self.attributes.append(Attribute("headboxHeight","number","Headbox height",default=0.0))
        self.attributes.append(Attribute("headboxRootChord","number","Headbox root chord",default=0.0))
        self.attributes.append(Attribute("headboxTipChord","number","Headbox tip chord",default=0.0))
        self.attributes.append(Attribute("headboxArea","number","Headbox area",default=0.0))
        self.attributes.append(Attribute("rudderHeight","number","Rudder height",default=0.0))
        self.attributes.append(Attribute("rudderRootChord","number","Rudder root chord",default=0.0))
        self.attributes.append(Attribute("rudderTipChord","number","Rudder tip chord",default=0.0))
        self.attributes.append(Attribute("rudderHornArea","number","Rudder horn area",default=0.0))
        self.attributes.append(Attribute("rudderTotalArea","number","Rudder total area (including horn)",default=0.0))
        self.attributes.append(Attribute("rudderPropellerHorizontalDistance","number","Horizontal distance from propeller plane to rudder stock",default=0.0))
        self.attributes.append(Attribute("rudderPropellerVerticalDistance","number","Vertical distance from propeller plane to rudder top",default=0.0))
        self.attributes.append(Attribute("rudderHeadboxGap","number","Initial gap between rudder and headbox",default=0.0))
        self.attributes.append(Attribute("wakeFraction","number","Wake fraction",default=0.0))
        self.attributes.append(Attribute("pitchRatio","number","Propeller pitch ratio",default=0.0))
        self.attributes.append(Attribute("bilgeRadius","number","Bilge radius",default=0.0))
        self.attributes.append(Attribute("verticalDistanceHull","number","Vertical distance from propeller center to hull",default=0.0))
        self.attributes.append(Attribute("thrustDeductionFactor","number","Thrust deduction factor",default=0.0))