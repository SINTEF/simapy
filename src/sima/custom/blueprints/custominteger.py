# 
# Generated with CustomIntegerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .parameterfield import ParameterFieldBlueprint

class CustomIntegerBlueprint(ParameterFieldBlueprint):
    """"""

    def __init__(self, name="CustomInteger", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("label","string","",default=""))
        self.attributes.append(Attribute("tooltip","string","",default=""))
        self.attributes.append(Attribute("value","integer","",default=0))
        self.attributes.append(Attribute("constraints","string","Give a valid range for a number: Use <,> for excluding and [] for including.\nExampless: \n- [0,4] Number from and including 0 to and including 4\n- <0,4> From and to, excluding \n- <,0> All negative numbers excluding 0\n- [0,> All positive numbers, including 0\n",default=""))