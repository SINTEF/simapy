# 
# Generated with SIMAApplicationPreferenceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .simapreference import SIMAPreferenceBlueprint

class SIMAApplicationPreferenceBlueprint(SIMAPreferenceBlueprint):
    """"""

    def __init__(self, name="SIMAApplicationPreference", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("createTimestamp","boolean","",default=True))
        self.add_attribute(Attribute("deleteAutomatically","boolean","",default=True))
        self.add_attribute(Attribute("interpolate","boolean","",default=True))
        self.add_attribute(Attribute("overrideTimeZone","boolean","",default=True))
        self.add_attribute(Attribute("minimumDiskSpace","integer","",default=1))
        self.add_attribute(Attribute("autoSaveFrequency","integer","",default=5))
        self.add_attribute(Attribute("backupFolder","string",""))
        self.add_attribute(Attribute("numberOfSignificantDigits","integer","Maximum number of significant digits used to display floating point numbers (editors must be reopened) ",default=5))