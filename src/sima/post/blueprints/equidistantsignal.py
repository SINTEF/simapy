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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("size","")))
        self.attributes.append(Attribute("directInput","boolean","",default=True))
        self.attributes.append(Attribute("values","number","",Dimension("size",""),default=0.0))
        self.attributes.append(Attribute("xunit","string","Defines the unit of the x axis",default='s'))
        self.attributes.append(Attribute("yunit","string","Defines the unit of the y axis",default='-'))
        self.attributes.append(Attribute("offset","number","The offset of the x axis.",default=0.0))
        self.attributes.append(Attribute("increment","number","The sample increment of the x axis",default=1.0))
        self.attributes.append(Attribute("size","integer","",default=0))
        self.attributes.append(Attribute("function","string","Apply the given function to each element of the input",default=""))