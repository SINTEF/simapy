# 
# Generated with ConditionTestBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .test import TestBlueprint

class ConditionTestBlueprint(TestBlueprint):
    """"""

    def __init__(self, name="ConditionTest", package_path="sima/doc", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("disabled","boolean","If disabled, the test will not be run in a continuous integration environment",default=False))
        self.add_attribute(EnumAttribute("duration","sima/doc/Duration",""))
        self.add_attribute(BlueprintAttribute("assertions","sima/doc/OutputNodeValueAssertion","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("comparisons","sima/doc/ComparisonAssertion","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("condition","sima/sima/Condition","",False))
        self.add_attribute(Attribute("analysis","string",""))