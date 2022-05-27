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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(Attribute("renameOutput","boolean","",default=True))
        self.attributes.append(EnumAttribute("operation","sima/post/StatisticsOperation",""))
        self.attributes.append(Attribute("combine","boolean","This will run the operation a second time on the transformed input to produce a combined output such as maxima of maxima etc.",default=False))
        self.attributes.append(BlueprintAttribute("inputSlot","sima/post/InputSlot","",True))
        self.attributes.append(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.attributes.append(Attribute("outputIndex","boolean","Output the index of the event ( valid for maxima and minima)",default=False))
        self.attributes.append(Attribute("combinedName","string","Name of output when using combined operation",default=""))