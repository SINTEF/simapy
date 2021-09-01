# 
# Generated with DistributionFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class DistributionFilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="DistributionFilter", package_path="sima/post", description=""):
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
        self.attributes.append(EnumAttribute("distribution","sima/post/Distribution","Number of intervals used for sample distribution"))
        self.attributes.append(Attribute("threshold","number","Threshold for fitting. Upper threshold when minima and lower threshold when maxima",default=0.0))
        self.attributes.append(Attribute("useReturnPeriod","boolean","Estimate return period value",default=False))
        self.attributes.append(Attribute("returnPeriod","number","Return period",default=3.0))
        self.attributes.append(Attribute("probabilityLevel","number","Compute response corresponding to the given probabilityLevel",default=0.5))
        self.attributes.append(EnumAttribute("extreme","sima/post/PeakExtreme","Maxima or minima distribution"))
        self.attributes.append(Attribute("transformAxis","boolean","Show output distribution in transformed axis",default=False))