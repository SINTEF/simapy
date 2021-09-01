# 
# Generated with DockingConeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class DockingConeBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="DockingCone", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("dampingExponent","number","Exponent of velocity in damping term",default=1.0))
        self.attributes.append(EnumAttribute("dampingInterpolation","sima/simo/Interpolation","Interpolation method for damping"))
        self.attributes.append(EnumAttribute("forceInterpolation","sima/simo/Interpolation","Interpolation method for force"))
        self.attributes.append(Attribute("velocityLimit","number","Velocity limit for friction force (Damping Exponent = 0)",default=0.0))
        self.attributes.append(Attribute("maxRadialDistance","number","Maximum radial distance at entry",default=0.0))
        self.attributes.append(Attribute("friction","number","Friction coefficient for sliding along the cone or cylinder surface",default=0.0))
        self.attributes.append(EnumAttribute("failureMode","sima/simo/ActivationFailureMode","Failure mode of coupling element"))
        self.attributes.append(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.attributes.append(Attribute("breakingStrength","number","Breaking strength",default=0.0))
        self.attributes.append(BlueprintAttribute("dockingPinBody","sima/simo/SIMOBody","",False))
        self.attributes.append(BlueprintAttribute("dockingPinPoint","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("dockingConePoint","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("dockingConeDirectionVector","sima/sima/Vector3","",True))
        self.attributes.append(BlueprintAttribute("dockingConeBody","sima/simo/SIMOBody","",False))
        self.attributes.append(BlueprintAttribute("crossSections","sima/simo/DockingConeCrossSection","",True,Dimension("size","")))