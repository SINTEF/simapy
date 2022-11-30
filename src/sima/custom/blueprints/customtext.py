# 
# Generated with CustomTextBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .parameterfield import ParameterFieldBlueprint
from sima.sima.blueprints.named import NamedBlueprint

class CustomTextBlueprint(ParameterFieldBlueprint,NamedBlueprint):
    """"""

    def __init__(self, name="CustomText", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("label","string",""))
        self.add_attribute(Attribute("tooltip","string",""))
        self.add_attribute(EnumAttribute("fileType","sima/custom/FileType",""))
        self.add_attribute(Attribute("directory","boolean","",default=False))
        self.add_attribute(Attribute("fileExtensions","string","Describes legal file extensions separated by semicolon, example:  *.txt;*.dat"))
        self.add_attribute(Attribute("options","string","",Dimension("*")))
        self.add_attribute(EnumAttribute("_type","sima/custom/FieldType",""))
        self.add_attribute(Attribute("width","integer","",default=10))
        self.add_attribute(Attribute("expandHorizontally","boolean","If set the field will fill all available horzontal space",default=False))
        self.add_attribute(Attribute("value","string",""))