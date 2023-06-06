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
        self.add_attribute(Attribute("inputCoordinateSystem","boolean","Specify the reference coordinate system by passing in a 3 or 6 dof position signal or a 9 dof rotation matrix (row order)",default=False))
        self.add_attribute(Attribute("offsetX","number","",default=0.0))
        self.add_attribute(Attribute("offsetY","number","",default=0.0))
        self.add_attribute(Attribute("offsetZ","number","",default=0.0))
        self.add_attribute(Attribute("rotationX","number","",default=0.0))
        self.add_attribute(Attribute("rotationY","number","",default=0.0))
        self.add_attribute(Attribute("rotationZ","number","",default=0.0))