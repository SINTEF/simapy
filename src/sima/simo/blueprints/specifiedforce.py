# 
# Generated with SpecifiedForceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class SpecifiedForceBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="SpecifiedForce", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(EnumAttribute("referenceFrame","sima/simo/ReferenceFrameType","Direction vector in local or global coordinate system"))
        self.add_attribute(BlueprintAttribute("directionVector","sima/sima/Vector3","",True))
        self.add_attribute(Attribute("activationTime","number","Time for switching component on",default=0.0))
        self.add_attribute(Attribute("deactivationTime","number","Time for switching component off",default=100000.0))
        self.add_attribute(EnumAttribute("loadType","sima/simo/SpecifiedLoadType",""))
        self.add_attribute(Attribute("period","number","",default=0.0))
        self.add_attribute(Attribute("phase","number","",default=0.0))
        self.add_attribute(Attribute("magnitude","number","Force component magnitude parameter",default=0.0))
        self.add_attribute(Attribute("forceDerivative","number","Force component force derivative parameter",default=0.0))
        self.add_attribute(BlueprintAttribute("attachmentPoint","sima/sima/Point3","",True))