# 
# Generated with ColumnConfigurationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .pathspecification import PathSpecificationBlueprint

class ColumnConfigurationBlueprint(PathSpecificationBlueprint):
    """"""

    def __init__(self, name="ColumnConfiguration", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("path","string","",default=""))
        self.attributes.append(Attribute("header","string","Column header. The default value is the header,legend or name attribute of the signal",default=""))
        self.attributes.append(Attribute("label","string","Column label. The default value is the unit of the y axis, or the label attribute, or ylabel + unit if specified",default=""))
        self.attributes.append(Attribute("format","string","Column number format. Please refer to https://docs.oracle.com/javase/tutorial/i18n/format/decimalFormat.html for a description",default='0.####E0'))
        self.attributes.append(Attribute("fontSize","integer","Column font size. Will be used when renderin the table in a report,etc.",default=0))