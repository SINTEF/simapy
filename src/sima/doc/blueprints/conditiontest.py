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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("disabled","boolean","If disabled, the test will not be run in a continuous integration environment",default=False))
        self.attributes.append(EnumAttribute("duration","sima/doc/Duration",""))
        self.attributes.append(BlueprintAttribute("assertions","sima/doc/OutputNodeValueAssertion","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("comparisons","sima/doc/ComparisonAssertion","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("condition","sima/sima/Condition","",False))
        self.attributes.append(Attribute("analysis","string","",default=""))