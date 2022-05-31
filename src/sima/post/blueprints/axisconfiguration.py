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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("font","sima/sima/FontDescription","",True))
        self.attributes.append(Attribute("log","boolean","",default=False))
        self.attributes.append(Attribute("autoFormat","boolean","",default=True))
        self.attributes.append(Attribute("format","string","",default='0.####E0'))
        self.attributes.append(Attribute("showGrid","boolean","",default=True))
        self.attributes.append(Attribute("dashGridLine","boolean","",default=False))
        self.attributes.append(Attribute("autoScale","boolean","",default=True))
        self.attributes.append(Attribute("minimum","number","",default=0.0))
        self.attributes.append(Attribute("maximum","number","",default=0.0))