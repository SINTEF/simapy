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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("model","sima/wamit/WamitModel","",False))
        self.attributes.append(BlueprintAttribute("body1","sima/wamit/WamitBodyResult","",False))
        self.attributes.append(BlueprintAttribute("body2","sima/wamit/WamitBodyResult","",False))
        self.attributes.append(BlueprintAttribute("radiationData","sima/hydro/CoupledRadiationDataGroup","",True))