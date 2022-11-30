# 
# Generated with IntegerValueBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .generatorsignal import GeneratorSignalBlueprint
from sima.sima.blueprints.singleparameter import SingleParameterBlueprint

class IntegerValueBlueprint(GeneratorSignalBlueprint,SingleParameterBlueprint):
    """"""

    def __init__(self, name="IntegerValue", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("array","boolean","",default=False))
        self.add_attribute(Attribute("value","integer","Value of the String constant",default=0))
        self.add_attribute(Attribute("values","integer","Value of the String constant",Dimension("*"),default=0))