# 
# Generated with HydrodynamicCouplingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class HydrodynamicCouplingBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="HydrodynamicCoupling", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("body1","sima/simo/SIMOBody","",False))
        self.attributes.append(BlueprintAttribute("body2","sima/simo/SIMOBody","",False))
        self.attributes.append(BlueprintAttribute("radiationData","sima/hydro/CoupledRadiationDataGroup","",True))