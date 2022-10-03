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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("showScripts","boolean","",default=False))
        self.attributes.append(Attribute("javaScriptLocations","string","",Dimension("*"),default=""))
        self.attributes.append(Attribute("pythonHome","string","Override python home folder",default=""))
        self.attributes.append(Attribute("pythonPaths","string","",Dimension("*"),default=""))