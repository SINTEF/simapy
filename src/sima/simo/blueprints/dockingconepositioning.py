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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("localPoint","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("globalPoint","sima/sima/Point3","",True))
        self.attributes.append(EnumAttribute("failureMode","sima/simo/ActivationFailureMode","Failure mode:\n - No failure\n - Failure by exceeding the breaking strength after specified time\n - Activation of element after specified time if absolute value of force is below breaking strength"))
        self.attributes.append(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.attributes.append(Attribute("breakingStrength","number","Breaking strength",default=0.0))
        self.attributes.append(Attribute("dampingExponent","number","Exponent of velocity in damping term",default=1.0))
        self.attributes.append(EnumAttribute("dampingInterpolation","sima/simo/Interpolation","Interpolation method for damping"))
        self.attributes.append(EnumAttribute("forceInterpolation","sima/simo/Interpolation","Interpolation method for force"))
        self.attributes.append(Attribute("velocityLimit","number","Velocity limit for friction force",default=0.0))
        self.attributes.append(Attribute("numberOfPoints","integer","",default=0))
        self.attributes.append(BlueprintAttribute("crossSections","sima/simo/DockingConeCrossSection","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("directionVector","sima/sima/Vector3","",True))
        self.attributes.append(Attribute("maxRadialDistance","number","Maximum radial distance at entry",default=0.0))
        self.attributes.append(Attribute("friction","number","Friction coefficient",default=0.0))