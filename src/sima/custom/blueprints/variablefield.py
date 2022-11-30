# 
# Generated with VariableFieldBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .parameterfield import ParameterFieldBlueprint

class VariableFieldBlueprint(ParameterFieldBlueprint):
    """"""

    def __init__(self, name="VariableField", package_path="sima/custom", description=""):
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
        self.add_attribute(BlueprintAttribute("variable","sima/sima/Variable","",False))
        self.add_attribute(Attribute("unit","string",""))
        self.add_attribute(Attribute("constraints","string","Give a valid range for a number: Use <,> for excluding and [] for including.\nExampless: \n- [0,4] Number from and including 0 to and including 4\n- <0,4> From and to, excluding \n- <,0> All negative numbers excluding 0\n- [0,> All positive numbers, including 0\n"))