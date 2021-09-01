# 
# Generated with FixedForceElongationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .positioningelement import PositioningElementBlueprint

class FixedForceElongationBlueprint(PositioningElementBlueprint):
    """"""

    def __init__(self, name="FixedForceElongation", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("localPoint","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("globalPoint","sima/sima/Point3","",True))
        self.attributes.append(EnumAttribute("failureMode","sima/simo/ActivationFailureMode","Failure mode:\n - No failure\n - Failure by exceeding the breaking strength after specified time\n - Activation of element after specified time if absolute value of force is below breaking strength"))
        self.attributes.append(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.attributes.append(Attribute("breakingStrength","number","Breaking strength",default=0.0))
        self.attributes.append(EnumAttribute("method","sima/simo/FixedForceElongationMethod","Method for initialisation of the fixed force elongation"))
        self.attributes.append(Attribute("pretension","number","Pretension",default=0.0))
        self.attributes.append(Attribute("direction","number","Direction of line in horizontal plane",default=0.0))
        self.attributes.append(Attribute("angle","number","Angle of line from horizontal plane (positive downwards)",default=0.0))
        self.attributes.append(Attribute("velocityLimit","number","Velocity limit for friction force (Damping Exponent = 0)",default=0.0))
        self.attributes.append(BlueprintAttribute("characteristic","sima/simo/ForceDampingCharacteristic","",True))