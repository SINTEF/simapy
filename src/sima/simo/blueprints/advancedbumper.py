# 
# Generated with AdvancedBumperBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class AdvancedBumperBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="AdvancedBumper", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("body1","sima/simo/SIMOBody","",False))
        self.attributes.append(BlueprintAttribute("body2","sima/simo/SIMOBody","",False))
        self.attributes.append(Attribute("velocityLimit","number","Velocity limit for friction force (Damping Exponent = 0)",default=0.0))
        self.attributes.append(BlueprintAttribute("characteristic","sima/simo/ForceDampingCharacteristic","",True))
        self.attributes.append(BlueprintAttribute("body1End1","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("body1End2","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("body2End1","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("body2End2","sima/sima/Point3","",True))