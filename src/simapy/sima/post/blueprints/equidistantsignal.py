# 
# Generated with EquidistantSignalBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .generatorsignal import GeneratorSignalBlueprint

class EquidistantSignalBlueprint(GeneratorSignalBlueprint):
    """"""

    def __init__(self, name="EquidistantSignal", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("directInput","boolean","",default=True))
        self.add_attribute(Attribute("values","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("xunit","string","Defines the unit of the x axis",default='s'))
        self.add_attribute(Attribute("yunit","string","Defines the unit of the y axis",default='-'))
        self.add_attribute(Attribute("offset","number","The offset of the x axis.",default=0.0))
        self.add_attribute(Attribute("increment","number","The sample increment of the x axis",default=1.0))
        self.add_attribute(Attribute("size","integer","",default=0))
        self.add_attribute(Attribute("function","string","Apply the given function to each element of the input"))