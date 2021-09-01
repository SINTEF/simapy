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
        self.attributes.append(EnumAttribute("extreme","sima/post/PeakExtreme","Get maxima or minima"))
        self.attributes.append(EnumAttribute("_type","sima/post/PeakType","Get local or global peaks"))
        self.attributes.append(Attribute("crossingLevel","number","Choose a crossing level",default=0.0))
        self.attributes.append(Attribute("useMean","boolean","Use mean value as crossing level",default=False))
        self.attributes.append(Attribute("partitions","integer","Number of partitions when finding block maxima/minima",default=10))