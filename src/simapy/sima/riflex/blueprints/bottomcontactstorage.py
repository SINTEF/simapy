# 
# Generated with BottomContactStorageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class BottomContactStorageBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BottomContactStorage", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("store","boolean","Store results for seafloor contact elements and / or soil layer profile (SLP) contact elements",default=False))
        self.add_attribute(Attribute("storageStep","integer","Code for storage of internal forces. Storage for every <storage step> given.",default=1))
        self.add_attribute(EnumAttribute("format","sima/riflex/FileFormatCode","Format code for additional output of time series"))
        self.add_attribute(BlueprintAttribute("forces","sima/riflex/BottomContactForceStorage","Specification of nodes for displacement storage",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("touchDownPoints","sima/riflex/TouchDownPointStorage","Specification of nodes for displacement storage",True,Dimension("*")))