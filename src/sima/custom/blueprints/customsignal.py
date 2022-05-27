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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("label","string","",default=""))
        self.attributes.append(Attribute("tooltip","string","",default=""))
        self.attributes.append(EnumAttribute("fileType","sima/custom/FileType",""))
        self.attributes.append(Attribute("directory","boolean","",default=False))
        self.attributes.append(Attribute("fileExtensions","string","Describes legal file extensions separated by semicolon, example:  *.txt;*.dat",default=""))
        self.attributes.append(Attribute("options","string","",Dimension("*"),default=""))
        self.attributes.append(EnumAttribute("_type","sima/custom/FieldType",""))
        self.attributes.append(Attribute("width","integer","",default=10))
        self.attributes.append(Attribute("expandHorizontally","boolean","If set the field will fill all available horzontal space",default=False))
        self.attributes.append(BlueprintAttribute("signal","sima/post/GeneratorSignal","",False))