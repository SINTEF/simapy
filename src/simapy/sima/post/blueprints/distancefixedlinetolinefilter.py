# 
# Generated with DistanceFixedLineToLineFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class DistanceFixedLineToLineFilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="DistanceFixedLineToLineFilter", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("renameOutput","boolean","",default=True))
        self.add_attribute(Attribute("xg1","number","X value of end 1 of global fixed line",default=0.0))
        self.add_attribute(Attribute("yg1","number","Y value of end 1 of global fixed line",default=0.0))
        self.add_attribute(Attribute("zg1","number","Z value of end 1 of global fixed line",default=0.0))
        self.add_attribute(Attribute("xg2","number","X value of end 2 of global fixed line",default=0.0))
        self.add_attribute(Attribute("yg2","number","Y value of end 2 of global fixed line",default=0.0))
        self.add_attribute(Attribute("zg2","number","Z value of end 2 of global fixed line",default=0.0))