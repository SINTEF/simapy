# 
# Generated with ElongationCharacteristicBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class ElongationCharacteristicBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="ElongationCharacteristic", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(EnumAttribute("inputType","sima/simo/ElongationCharacteristicType","Elongation characteristic type. Stress-strain or tension-strain."))
        self.add_attribute(BlueprintAttribute("items","sima/simo/ElongationItem","",True,Dimension("*")))
        self.add_attribute(Attribute("tensionMax","number","Historical maximum tension",default=0.0))
        self.add_attribute(BlueprintAttribute("fibreRopeModel","sima/simo/FibreRopeModel","",False))