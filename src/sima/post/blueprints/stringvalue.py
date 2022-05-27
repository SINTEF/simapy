# 
# Generated with StringValueBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .generatorsignal import GeneratorSignalBlueprint
from sima.sima.blueprints.singleparameter import SingleParameterBlueprint

class StringValueBlueprint(GeneratorSignalBlueprint,SingleParameterBlueprint):
    """"""

    def __init__(self, name="StringValue", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.attributes.append(Attribute("array","boolean","",default=False))
        self.attributes.append(Attribute("value","string","Value of the String constant",default=""))
        self.attributes.append(Attribute("values","string","Value of the String constant",Dimension("*"),default=""))