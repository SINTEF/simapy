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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("velocityLimit","number","Velocity limit for damping force",default=0.0))
        self.add_attribute(BlueprintAttribute("characteristic","sima/simo/ForceDampingCharacteristic","",True))
        self.add_attribute(BlueprintAttribute("bodyEnd1","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("bodyEnd2","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("globalEnd1","sima/sima/Point3","",True))
        self.add_attribute(BlueprintAttribute("globalEnd2","sima/sima/Point3","",True))