# 
# Generated with ReportFragmentNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...post.blueprints.runnode import RunNodeBlueprint
from ...report.blueprints.reportfragmentreference import ReportFragmentReferenceBlueprint

class ReportFragmentNodeBlueprint(RunNodeBlueprint,ReportFragmentReferenceBlueprint):
    """"""

    def __init__(self, name="ReportFragmentNode", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("root","sima/workflow/ReportFragmentItemContainer","",True))
        self.add_attribute(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))