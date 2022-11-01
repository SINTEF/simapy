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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("severity","sima/sima/Severity",""))
        self.attributes.append(Attribute("message","string","",default=""))
        self.attributes.append(BlueprintAttribute("outputNode","sima/post/OutputNode","",False))
        self.attributes.append(Attribute("path","string","",default=""))
        self.attributes.append(Attribute("expectedValue","string","When expected value is a number, the number of significant digits will be used as a tolerance level",default=""))
        self.attributes.append(Attribute("tolerance","number","When set, will be used instead of the implicit toleranse based on significant digits",default=0.0))