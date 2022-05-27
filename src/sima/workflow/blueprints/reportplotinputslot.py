# 
# Generated with ReportPlotInputSlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .reportfragmentitem import ReportFragmentItemBlueprint
from sima.post.blueprints.inputslot import InputSlotBlueprint

class ReportPlotInputSlotBlueprint(ReportFragmentItemBlueprint,InputSlotBlueprint):
    """"""

    def __init__(self, name="ReportPlotInputSlot", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("caption","string","",default=""))
        self.attributes.append(Attribute("width","integer","",default=0))
        self.attributes.append(Attribute("height","integer","",default=0))