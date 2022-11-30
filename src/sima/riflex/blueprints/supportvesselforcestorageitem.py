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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("vessel","sima/riflex/SupportVessel","",False))
        self.add_attribute(EnumAttribute("referenceSystem","sima/riflex/BodyForceReferenceSystem",""))