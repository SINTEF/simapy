# 
# Generated with TimeDependentPointMassBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class TimeDependentPointMassBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="TimeDependentPointMass", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("point","sima/sima/Point3","Mass point (local coordinates).",True))
        self.add_attribute(BlueprintAttribute("flowRates","sima/simo/FlowRateItem","",True,Dimension("*")))
        self.add_attribute(Attribute("mass0","number","Mass at t=0 (may be negative).",default=0.0))
        self.add_attribute(Attribute("massMax","number","Maximum allowable mass Mass, (may be negative).",default=0.0))
        self.add_attribute(Attribute("massMin","number","Minimum allowable mass Mass, (may be negative).",default=0.0))
        self.add_attribute(Attribute("massRateMax","number","Maximum allowable mass rate, (may be negative) (HLA only).",default=0.0))
        self.add_attribute(Attribute("massRateMin","number","Minimum allowable mass rate, (may be negative) (HLA only).",default=0.0))