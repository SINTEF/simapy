# 
# Generated with SupportVesselForceStorageItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SupportVesselForceStorageItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SupportVesselForceStorageItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("vessel","sima/riflex/SupportVessel","",False))
        self.attributes.append(EnumAttribute("referenceSystem","sima/riflex/BodyForceReferenceSystem",""))