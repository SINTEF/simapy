# 
# Generated with CustomSignalBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .customcomponent import CustomComponentBlueprint

class CustomSignalBlueprint(CustomComponentBlueprint):
    """"""

    def __init__(self, name="CustomSignal", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("label","string",""))
        self.add_attribute(Attribute("tooltip","string",""))
        self.add_attribute(EnumAttribute("fileType","sima/custom/FileType",""))
        self.add_attribute(Attribute("directory","boolean","",default=False))
        self.add_attribute(Attribute("fileExtensions","string","Describes legal file extensions separated by semicolon, example:  *.txt;*.dat"))
        self.add_attribute(Attribute("options","string","",Dimension("*")))
        self.add_attribute(EnumAttribute("_type","sima/custom/FieldType",""))
        self.add_attribute(Attribute("width","integer","",default=10))
        self.add_attribute(Attribute("expandHorizontally","boolean","If set the field will fill all available horzontal space",default=False))
        self.add_attribute(BlueprintAttribute("signal","sima/post/GeneratorSignal","",False))