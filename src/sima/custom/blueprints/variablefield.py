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
        self.attributes.append(BlueprintAttribute("variable","sima/sima/Variable","",False))
        self.attributes.append(Attribute("unit","string","",default=""))
        self.attributes.append(Attribute("constraints","string","Give a valid range for a number: Use <,> for excluding and [] for including.\nExampless: \n- [0,4] Number from and including 0 to and including 4\n- <0,4> From and to, excluding \n- <,0> All negative numbers excluding 0\n- [0,> All positive numbers, including 0\n",default=""))