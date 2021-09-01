# 
# Generated with ConstantValueBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .generatorsignal import GeneratorSignalBlueprint
from sima.sima.blueprints.singleparameter import SingleParameterBlueprint

class ConstantValueBlueprint(GeneratorSignalBlueprint,SingleParameterBlueprint):
    """"""

    def __init__(self, name="ConstantValue", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("size","")))
        self.attributes.append(Attribute("value","number","Value of the constant",default=0.0))
        self.attributes.append(Attribute("unit","string","Defines the unit of the constant",default='-'))