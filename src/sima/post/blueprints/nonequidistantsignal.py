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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.attributes.append(Attribute("xunit","string","Defines the unit of the x axis",default='s'))
        self.attributes.append(Attribute("yunit","string","Defines the unit of the y axis",default='-'))
        self.attributes.append(BlueprintAttribute("values","sima/post/XYItem","",True,Dimension("*")))
        self.attributes.append(Attribute("ylabel","string","",default=""))
        self.attributes.append(Attribute("xlabel","string","",default=""))