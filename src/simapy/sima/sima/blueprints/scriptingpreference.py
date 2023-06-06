# 
# Generated with ScriptingPreferenceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .simapreference import SIMAPreferenceBlueprint

class ScriptingPreferenceBlueprint(SIMAPreferenceBlueprint):
    """"""

    def __init__(self, name="ScriptingPreference", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("showScripts","boolean","",default=False))
        self.add_attribute(Attribute("javaScriptLocations","string","",Dimension("*")))
        self.add_attribute(Attribute("pythonHome","string","Override python home folder"))
        self.add_attribute(Attribute("pythonPaths","string","",Dimension("*")))