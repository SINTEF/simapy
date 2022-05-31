# 
# Generated with SNCurveBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class SNCurveBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="SNCurve", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("usePredefinedCurve","boolean","Use predefined SN-curve from selected standard",default=False))
        self.attributes.append(EnumAttribute("predefinedCurve","sima/post/SNCurveType",""))
        self.attributes.append(Attribute("negativeInverseSlope","number","Negative inverse slope of the segment (first segment if several segments are given, or total curve if no more are given)",default=0.0))
        self.attributes.append(Attribute("interceptStress","number","Stress range resulting in failure after one cycle",default=0.0))
        self.attributes.append(Attribute("thicknessExponent","number","Thickness exponent on fatigue strength",default=1.0))
        self.attributes.append(Attribute("referenceThicknessFactor","number","t/t_ref:  where t is thickness through which a crack will most likely grow and t_ref i reference thickness",default=1.0))
        self.attributes.append(BlueprintAttribute("curveItems","sima/post/SNCurveItem","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("fatigueLimitIndicator","sima/post/FatigueLimitIndicator",""))
        self.attributes.append(Attribute("fatigueLimitStress","number","Stress range level for which the SN curve becomes horizontal.",default=0.0))
        self.attributes.append(Attribute("fatigueLimitCycles","number","Logarithm of number of stress cycles for which the SN curve becomes horizontal.",default=0.0))