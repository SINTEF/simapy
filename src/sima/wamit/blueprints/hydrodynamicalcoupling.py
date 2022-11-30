# 
# Generated with HydrodynamicalCouplingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class HydrodynamicalCouplingBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="HydrodynamicalCoupling", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("model","sima/wamit/WamitModel","",False))
        self.add_attribute(BlueprintAttribute("body1","sima/wamit/WamitBodyResult","",False))
        self.add_attribute(BlueprintAttribute("body2","sima/wamit/WamitBodyResult","",False))
        self.add_attribute(BlueprintAttribute("radiationData","sima/hydro/CoupledRadiationDataGroup","",True))