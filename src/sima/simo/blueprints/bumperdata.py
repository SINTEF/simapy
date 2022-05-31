# 
# Generated with BumperDataBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class BumperDataBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="BumperData", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("velocityLimit","number","Velocity limit for damping force",default=0.0))
        self.attributes.append(BlueprintAttribute("characteristic","sima/simo/ForceDampingCharacteristic","",True))
        self.attributes.append(BlueprintAttribute("bodyEnd1","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("bodyEnd2","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("globalEnd1","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("globalEnd2","sima/sima/Point3","",True))