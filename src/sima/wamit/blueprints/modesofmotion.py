# 
# Generated with ModesOfMotionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ModesOfMotionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ModesOfMotion", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("surge","boolean","",default=True))
        self.add_attribute(Attribute("sway","boolean","",default=True))
        self.add_attribute(Attribute("heave","boolean","",default=True))
        self.add_attribute(Attribute("roll","boolean","",default=True))
        self.add_attribute(Attribute("pitch","boolean","",default=True))
        self.add_attribute(Attribute("yaw","boolean","",default=True))