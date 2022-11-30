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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("dampingExponent","number","Exponent of velocity in damping term",default=1.0))
        self.add_attribute(EnumAttribute("dampingInterpolation","sima/simo/Interpolation","Interpolation method for damping"))
        self.add_attribute(EnumAttribute("forceInterpolation","sima/simo/Interpolation","Interpolation method for force"))
        self.add_attribute(Attribute("velocityLimit","number","Velocity limit for friction force (Damping Exponent = 0)",default=0.0))
        self.add_attribute(Attribute("maxRadialDistance","number","Maximum radial distance at entry",default=0.0))
        self.add_attribute(Attribute("friction","number","Friction coefficient for sliding along the cone or cylinder surface",default=0.0))
        self.add_attribute(EnumAttribute("failureMode","sima/simo/ActivationFailureMode","Failure mode of coupling element"))
        self.add_attribute(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.add_attribute(Attribute("breakingStrength","number","Breaking strength",default=0.0))
        self.add_attribute(BlueprintAttribute("dockingPinBody","sima/simo/SIMOBody","",False))
        self.add_attribute(BlueprintAttribute("dockingPinPoint","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("dockingConePoint","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("dockingConeDirectionVector","sima/sima/Vector3","",True))
        self.add_attribute(BlueprintAttribute("dockingConeBody","sima/simo/SIMOBody","",False))
        self.add_attribute(BlueprintAttribute("crossSections","sima/simo/DockingConeCrossSection","",True,Dimension("*")))