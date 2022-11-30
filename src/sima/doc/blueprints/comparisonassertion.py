# 
# Generated with ComparisonAssertionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ComparisonAssertionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ComparisonAssertion", package_path="sima/doc", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("severity","sima/sima/Severity",""))
        self.add_attribute(Attribute("message","string",""))
        self.add_attribute(BlueprintAttribute("outputNode","sima/post/OutputNode","",False))
        self.add_attribute(Attribute("path","string",""))
        self.add_attribute(Attribute("read","boolean","If the path points to a file, the file will be read",default=False))
        self.add_attribute(Attribute("expectedOutput","string","Expected output represented by the content of this file"))