# 
# Generated with VersioningPreferenceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .simapreference import SIMAPreferenceBlueprint

class VersioningPreferenceBlueprint(SIMAPreferenceBlueprint):
    """"""

    def __init__(self, name="VersioningPreference", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("userHome","string","Override user home folder"))
        self.add_attribute(Attribute("sshFolder","string","Override ssh folder"))