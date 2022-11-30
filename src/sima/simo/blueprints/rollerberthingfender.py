# 
# Generated with RollerBerthingFenderBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class RollerBerthingFenderBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="RollerBerthingFender", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("dynamicFriction","number","Dynamic friction coefficient, sliding",default=0.0))
        self.add_attribute(Attribute("staticFriction","number","Friction coefficient, when not sliding (stiction)",default=0.0))
        self.add_attribute(Attribute("shearStiffnes","number","Shear stiffness associated with friction",default=0.0))
        self.add_attribute(Attribute("velocityLimit","number","Velocity limit for normal friction force",default=0.0))
        self.add_attribute(BlueprintAttribute("contactPlane","sima/simo/Plane","",True))
        self.add_attribute(BlueprintAttribute("characteristic","sima/simo/ForceDampingCharacteristic","",True))
        self.add_attribute(EnumAttribute("attachment","sima/simo/FenderAttachment","Fender attachment"))
        self.add_attribute(BlueprintAttribute("contactPoint","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("axisVector","sima/sima/Vector3","",True))