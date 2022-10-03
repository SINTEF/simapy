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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("createTimestamp","boolean","",default=True))
        self.attributes.append(Attribute("deleteAutomatically","boolean","",default=True))
        self.attributes.append(Attribute("interpolate","boolean","",default=True))
        self.attributes.append(Attribute("overrideTimeZone","boolean","",default=True))
        self.attributes.append(Attribute("minimumDiskSpace","integer","",default=1))
        self.attributes.append(Attribute("autoSaveFrequency","integer","",default=5))
        self.attributes.append(Attribute("backupFolder","string","",default=""))
        self.attributes.append(Attribute("numberOfSignificantDigits","integer","Maximum number of significant digits used to display floating point numbers (editors must be reopened) ",default=5))