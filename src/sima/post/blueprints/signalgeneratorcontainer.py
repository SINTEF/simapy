# 
# Generated with SignalGeneratorContainerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .signalpropertiescontainer import SignalPropertiesContainerBlueprint
from sima.sima.blueprints.named import NamedBlueprint

class SignalGeneratorContainerBlueprint(SignalPropertiesContainerBlueprint,NamedBlueprint):
    """"""

    def __init__(self, name="SignalGeneratorContainer", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("signals","sima/post/GeneratorSignal","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("children","sima/post/SignalGeneratorContainer","",True,Dimension("*")))