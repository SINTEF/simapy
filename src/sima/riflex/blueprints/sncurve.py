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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(EnumAttribute("fatigueLimitIndicator","sima/riflex/FatigueLimitIndicator","Fatigue limit indicator"))
        self.add_attribute(Attribute("fatigueLimit","number","Point where SN curve becomes horizontal. Stresses below this line will not contribute to fatigue damage.",default=0.0))
        self.add_attribute(Attribute("referenceThickness","number","Reference thickness for thickness correction. A value of zero will give no thickness correction.",default=0.0))
        self.add_attribute(Attribute("thicknessCorrectionExponent","number","Exponent for thickness correction",default=0.0))
        self.add_attribute(Attribute("firstSlope","number","Slope of the SN curve - m",default=0.0))
        self.add_attribute(Attribute("constant","number","Constant defining the SN curve. First segment or total curve - logC (for a SN-curve given in MPa)",default=0.0))
        self.add_attribute(BlueprintAttribute("curveItems","sima/riflex/SNCurveItem","",True,Dimension("*")))