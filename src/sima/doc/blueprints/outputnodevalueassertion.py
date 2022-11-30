# 
# Generated with OutputNodeValueAssertionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class OutputNodeValueAssertionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="OutputNodeValueAssertion", package_path="sima/doc", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("severity","sima/sima/Severity",""))
        self.add_attribute(Attribute("message","string",""))
        self.add_attribute(BlueprintAttribute("outputNode","sima/post/OutputNode","",False))
        self.add_attribute(Attribute("path","string",""))
        self.add_attribute(Attribute("expectedValue","string","When expected value is a number, the number of significant digits will be used as a tolerance level"))
        self.add_attribute(Attribute("tolerance","number","When set, will be used instead of the implicit toleranse based on significant digits",default=0.0))