# 
# Generated with WindowFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class WindowFilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="WindowFilter", package_path="sima/post", description=""):
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
        self.attributes.append(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("size","")))
        self.attributes.append(Attribute("renameOutput","boolean","",default=True))
        self.attributes.append(Attribute("useIndex","boolean","Specify start and end index of signal",default=True))
        self.attributes.append(Attribute("start","number","",default=0.0))
        self.attributes.append(Attribute("end","number","",default=0.0))
        self.attributes.append(Attribute("setStartValue","boolean","",default=True))
        self.attributes.append(Attribute("startValue","number","",default=0.0))
        self.attributes.append(Attribute("startIndex","integer","",default=0))
        self.attributes.append(Attribute("endIndex","integer","End index or last index if not set",default=0))