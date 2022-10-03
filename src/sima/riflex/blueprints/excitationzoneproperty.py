# 
# Generated with ExcitationZonePropertyBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class ExcitationZonePropertyBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="ExcitationZoneProperty", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("min","number","Minimum non dimensional frequency limit",default=0.125))
        self.attributes.append(Attribute("max","number","Minimum non dimensional frequency limit",default=0.2))