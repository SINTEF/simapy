# 
# Generated with AxisConfigurationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class AxisConfigurationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="AxisConfiguration", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("font","sima/sima/FontDescription","",True))
        self.add_attribute(Attribute("log","boolean","",default=False))
        self.add_attribute(Attribute("autoFormat","boolean","",default=True))
        self.add_attribute(Attribute("format","string","",default='0.####E0'))
        self.add_attribute(Attribute("showGrid","boolean","",default=True))
        self.add_attribute(Attribute("dashGridLine","boolean","",default=False))
        self.add_attribute(Attribute("autoScale","boolean","",default=True))
        self.add_attribute(Attribute("minimum","number","",default=0.0))
        self.add_attribute(Attribute("maximum","number","",default=0.0))