# 
# Generated with RotationMatrixBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class RotationMatrixBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="RotationMatrix", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.add_attribute(Attribute("rotationX","number","Rotation about new x-axis (third rotation)",default=0.0))
        self.add_attribute(Attribute("rotationY","number","Rotation about new y-axis (second rotation)",default=0.0))
        self.add_attribute(Attribute("rotationZ","number","Rotation about z-axis (first rotation)",default=0.0))
        self.add_attribute(Attribute("transpose","boolean","Transpose (invert) the input reference rotation matrix before performing the transformation",default=False))
        self.add_attribute(Attribute("inputRotations","boolean","Input the euler angles",default=False))
        self.add_attribute(BlueprintAttribute("rotationInput","sima/post/InputSlot","",True))