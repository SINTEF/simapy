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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("inputType","sima/simo/ElongationCharacteristicType","Elongation characteristic type. Stress-strain or tension-strain."))
        self.attributes.append(BlueprintAttribute("items","sima/simo/ElongationItem","",True,Dimension("size","")))
        self.attributes.append(Attribute("tensionMax","number","Historical maximum tension",default=0.0))
        self.attributes.append(BlueprintAttribute("fibreRopeModel","sima/simo/FibreRopeModel","",False))