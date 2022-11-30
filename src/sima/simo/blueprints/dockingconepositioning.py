# 
# Generated with DockingConePositioningBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .positioningelement import PositioningElementBlueprint

class DockingConePositioningBlueprint(PositioningElementBlueprint):
    """"""

    def __init__(self, name="DockingConePositioning", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("localPoint","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("globalPoint","sima/sima/Point3","",True))
        self.add_attribute(EnumAttribute("failureMode","sima/simo/ActivationFailureMode","Failure mode:\n - No failure\n - Failure by exceeding the breaking strength after specified time\n - Activation of element after specified time if absolute value of force is below breaking strength"))
        self.add_attribute(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.add_attribute(Attribute("breakingStrength","number","Breaking strength",default=0.0))
        self.add_attribute(Attribute("dampingExponent","number","Exponent of velocity in damping term",default=1.0))
        self.add_attribute(EnumAttribute("dampingInterpolation","sima/simo/Interpolation","Interpolation method for damping"))
        self.add_attribute(EnumAttribute("forceInterpolation","sima/simo/Interpolation","Interpolation method for force"))
        self.add_attribute(Attribute("velocityLimit","number","Velocity limit for friction force",default=0.0))
        self.add_attribute(Attribute("numberOfPoints","integer","",default=0))
        self.add_attribute(BlueprintAttribute("crossSections","sima/simo/DockingConeCrossSection","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("directionVector","sima/sima/Vector3","",True))
        self.add_attribute(Attribute("maxRadialDistance","number","Maximum radial distance at entry",default=0.0))
        self.add_attribute(Attribute("friction","number","Friction coefficient",default=0.0))