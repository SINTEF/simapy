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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("surge","boolean","",default=True))
        self.attributes.append(Attribute("sway","boolean","",default=True))
        self.attributes.append(Attribute("heave","boolean","",default=True))
        self.attributes.append(Attribute("roll","boolean","",default=True))
        self.attributes.append(Attribute("pitch","boolean","",default=True))
        self.attributes.append(Attribute("yaw","boolean","",default=True))