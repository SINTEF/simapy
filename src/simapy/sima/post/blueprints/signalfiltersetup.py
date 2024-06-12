# 
# Generated with SignalFilterSetupBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class SignalFilterSetupBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SignalFilterSetup", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("start","number","",default=0.0))
        self.add_attribute(Attribute("end","number","",default=0.0))
        self.add_attribute(EnumAttribute("filtering","sima/post/Filtering","Filter signal using lower and upper cut off"))
        self.add_attribute(Attribute("lowerCutoffFrequency","number","",default=0.0))
        self.add_attribute(Attribute("upperCutoffFrequency","number","",default=0.0))
        self.add_attribute(Attribute("showFullPath","boolean","Show full path when selecting signals",default=False))