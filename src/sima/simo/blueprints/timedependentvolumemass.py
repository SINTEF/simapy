# 
# Generated with TimeDependentVolumeMassBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class TimeDependentVolumeMassBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="TimeDependentVolumeMass", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("point","sima/sima/Point3","Mass point (local coordinates).",True))
        self.add_attribute(BlueprintAttribute("flowRates","sima/simo/FlowRateItem","",True,Dimension("*")))
        self.add_attribute(Attribute("vol0","number","Volume of liquid at t=0",default=0.0))
        self.add_attribute(Attribute("volMax","number","Maximum allowable volume",default=0.0))
        self.add_attribute(Attribute("volMin","number","Minimum allowable volume",default=0.0))
        self.add_attribute(Attribute("volRateMax","number","Maximum allowable volume rate (HLA only)",default=0.0))
        self.add_attribute(Attribute("volRateMin","number","Minimum allowable volume rate (HLA only)",default=0.0))
        self.add_attribute(Attribute("density","number","Density of liquid in tank",default=0.0))
        self.add_attribute(BlueprintAttribute("vectorZ","sima/sima/Vector3","Vector defining portion z-axis in local system",True))
        self.add_attribute(BlueprintAttribute("vectorXZ","sima/sima/Vector3","Vector in local xz-plane def. portion x-axis",True))
        self.add_attribute(BlueprintAttribute("portions","sima/simo/VolumeMassPortion","",True,Dimension("*")))