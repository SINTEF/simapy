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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.attributes.append(Attribute("rotationX","number","Rotation about new x-axis (third rotation)",default=0.0))
        self.attributes.append(Attribute("rotationY","number","Rotation about new y-axis (second rotation)",default=0.0))
        self.attributes.append(Attribute("rotationZ","number","Rotation about z-axis (first rotation)",default=0.0))
        self.attributes.append(Attribute("transpose","boolean","Transpose (invert) the input reference rotation matrix before performing the transformation",default=False))
        self.attributes.append(Attribute("inputRotations","boolean","Input the euler angles",default=False))
        self.attributes.append(BlueprintAttribute("rotationInput","sima/post/InputSlot","",True))