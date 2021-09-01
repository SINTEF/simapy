# 
# Generated with ReportFragmentNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.report.blueprints.reportfragmentreference import ReportFragmentReferenceBlueprint
from sima.post.blueprints.runnode import RunNodeBlueprint

class ReportFragmentNodeBlueprint(ReportFragmentReferenceBlueprint,RunNodeBlueprint):
    """"""

    def __init__(self, name="ReportFragmentNode", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("root","sima/workflow/ReportFragmentItemContainer","",True))
        self.attributes.append(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))