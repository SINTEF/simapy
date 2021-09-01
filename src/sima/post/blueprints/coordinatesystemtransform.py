# 
# Generated with CoordinateSystemTransformBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class CoordinateSystemTransformBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="CoordinateSystemTransform", package_path="sima/post", description=""):
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
        self.attributes.append(Attribute("inputCoordinateSystem","boolean","Specify the reference coordinate system by passing in a 3 or 6 dof position signal or a 9 dof rotation matrix (row order)",default=False))
        self.attributes.append(Attribute("offsetX","number","",default=0.0))
        self.attributes.append(Attribute("offsetY","number","",default=0.0))
        self.attributes.append(Attribute("offsetZ","number","",default=0.0))
        self.attributes.append(Attribute("rotationX","number","",default=0.0))
        self.attributes.append(Attribute("rotationY","number","",default=0.0))
        self.attributes.append(Attribute("rotationZ","number","",default=0.0))