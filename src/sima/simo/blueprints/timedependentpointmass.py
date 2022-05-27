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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("point","sima/sima/Point3","Mass point (local coordinates).",True))
        self.attributes.append(BlueprintAttribute("flowRates","sima/simo/FlowRateItem","",True,Dimension("*")))
        self.attributes.append(Attribute("mass0","number","Mass at t=0 (may be negative).",default=0.0))
        self.attributes.append(Attribute("massMax","number","Maximum allowable mass Mass, (may be negative).",default=0.0))
        self.attributes.append(Attribute("massMin","number","Minimum allowable mass Mass, (may be negative).",default=0.0))
        self.attributes.append(Attribute("massRateMax","number","Maximum allowable mass rate, (may be negative) (HLA only).",default=0.0))
        self.attributes.append(Attribute("massRateMin","number","Minimum allowable mass rate, (may be negative) (HLA only).",default=0.0))