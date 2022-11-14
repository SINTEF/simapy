# 
# Generated with PeaksFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class PeaksFilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="PeaksFilter", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("_id","string","",default=None))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string","",default=None))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("renameOutput","boolean","",default=True))
        self.add_attribute(EnumAttribute("extreme","sima/post/PeakExtreme","Get maxima or minima"))
        self.add_attribute(EnumAttribute("_type","sima/post/PeakType","Get local or global peaks"))
        self.add_attribute(Attribute("crossingLevel","number","Choose a crossing level",default=0.0))
        self.add_attribute(Attribute("useMean","boolean","Use mean value as crossing level",default=False))
        self.add_attribute(Attribute("partitions","integer","Number of partitions when finding block maxima/minima",default=10))