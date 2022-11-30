# 
# Generated with NonEquidistantSignalBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .generatorsignal import GeneratorSignalBlueprint

class NonEquidistantSignalBlueprint(GeneratorSignalBlueprint):
    """"""

    def __init__(self, name="NonEquidistantSignal", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("xunit","string","Defines the unit of the x axis",default='s'))
        self.add_attribute(Attribute("yunit","string","Defines the unit of the y axis",default='-'))
        self.add_attribute(BlueprintAttribute("values","sima/post/XYItem","",True,Dimension("*")))
        self.add_attribute(Attribute("ylabel","string",""))
        self.add_attribute(Attribute("xlabel","string",""))