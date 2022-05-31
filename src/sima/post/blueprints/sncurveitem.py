# 
# Generated with SNCurveItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SNCurveItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SNCurveItem", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("negativeInverseSlope","number","Negative inverse slope of S-N curve",default=0.0))
        self.attributes.append(Attribute("transitionPointLog","number","log10 of number of cycles at transition point between preceding curve segment and this curve segment",default=0.0))