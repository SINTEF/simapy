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

    def __init__(self, name="SNCurve", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("fatigueLimitIndicator","sima/riflex/FatigueLimitIndicator","Fatigue limit indicator"))
        self.attributes.append(Attribute("fatigueLimit","number","Point where SN curve becomes horizontal. Stresses below this line will not contribute to fatigue damage.",default=0.0))
        self.attributes.append(Attribute("referenceThickness","number","Reference thickness for thickness correction. A value of zero will give no thickness correction.",default=0.0))
        self.attributes.append(Attribute("thicknessCorrectionExponent","number","Exponent for thickness correction",default=0.0))
        self.attributes.append(Attribute("firstSlope","number","Slope of the SN curve - m",default=0.0))
        self.attributes.append(Attribute("constant","number","Constant defining the SN curve. First segment or total curve - logC (for a SN-curve given in MPa)",default=0.0))
        self.attributes.append(BlueprintAttribute("curveItems","sima/riflex/SNCurveItem","",True,Dimension("size","")))