# 
# Generated with PointBerthingFenderBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class PointBerthingFenderBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="PointBerthingFender", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("dynamicFriction","number","Dynamic friction coefficient, sliding",default=0.0))
        self.attributes.append(Attribute("staticFriction","number","Friction coefficient, when not sliding (stiction)",default=0.0))
        self.attributes.append(Attribute("shearStiffnes","number","Shear stiffness associated with friction",default=0.0))
        self.attributes.append(Attribute("velocityLimit","number","Velocity limit for normal friction force",default=0.0))
        self.attributes.append(BlueprintAttribute("contactPlane","sima/simo/Plane","",True))
        self.attributes.append(BlueprintAttribute("characteristic","sima/simo/ForceDampingCharacteristic","",True))
        self.attributes.append(EnumAttribute("attachment","sima/simo/FenderAttachment","Fender attachment"))
        self.attributes.append(BlueprintAttribute("contactPoint","sima/sima/Point3","",True))