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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("referenceFrame","sima/simo/ReferenceFrameType","Direction vector in local or global coordinate system"))
        self.attributes.append(BlueprintAttribute("directionVector","sima/sima/Vector3","",True))
        self.attributes.append(Attribute("activationTime","number","Time for switching component on",default=0.0))
        self.attributes.append(Attribute("deactivationTime","number","Time for switching component off",default=100000.0))
        self.attributes.append(EnumAttribute("loadType","sima/simo/SpecifiedLoadType",""))
        self.attributes.append(Attribute("period","number","",default=0.0))
        self.attributes.append(Attribute("phase","number","",default=0.0))
        self.attributes.append(Attribute("magnitude","number","Force component magnitude parameter",default=0.0))
        self.attributes.append(Attribute("forceDerivative","number","Force component force derivative parameter",default=0.0))
        self.attributes.append(BlueprintAttribute("attachmentPoint","sima/sima/Point3","",True))