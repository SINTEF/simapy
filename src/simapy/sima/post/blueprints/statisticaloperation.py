# 
# Generated with StatisticalOperationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class StatisticalOperationBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="StatisticalOperation", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("renameOutput","boolean","",default=True))
        self.add_attribute(EnumAttribute("operation","sima/post/StatisticsOperation",""))
        self.add_attribute(Attribute("combine","boolean","This will run the operation a second time on the transformed input to produce a combined output such as maxima of maxima etc.",default=False))
        self.add_attribute(BlueprintAttribute("inputSlot","sima/post/InputSlot","",True))
        self.add_attribute(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.add_attribute(Attribute("outputIndex","boolean","Output the index of the event ( valid for maxima and minima)",default=False))
        self.add_attribute(Attribute("combinedName","string","Name of output when using combined operation"))