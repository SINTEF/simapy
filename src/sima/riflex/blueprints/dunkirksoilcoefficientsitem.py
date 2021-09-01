# 
# Generated with DunkirkSoilCoefficientsItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .commonsoilcoefficientsitem import CommonSoilCoefficientsItemBlueprint

class DunkirkSoilCoefficientsItemBlueprint(CommonSoilCoefficientsItemBlueprint):
    """"""

    def __init__(self, name="DunkirkSoilCoefficientsItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("c1","number","",default=0.0))
        self.attributes.append(Attribute("c2","number","",default=0.0))
        self.attributes.append(Attribute("c3","number","",default=0.0))
        self.attributes.append(Attribute("c4","number","",default=0.0))