# 
# Generated with TableFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint
from .signaltable import SignalTableBlueprint

class TableFilterBlueprint(OperationNodeBlueprint,SignalTableBlueprint):
    """"""

    def __init__(self, name="TableFilter", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("*")))
        self.attributes.append(Attribute("renameOutput","boolean","",default=True))
        self.attributes.append(BlueprintAttribute("columns","sima/post/ColumnConfiguration","",True,Dimension("*")))
        self.attributes.append(Attribute("fixed","boolean","",default=False))
        self.attributes.append(Attribute("transposed","boolean","",default=False))
        self.attributes.append(Attribute("allInputs","boolean","",default=False))