# 
# Generated with DirectionDependentScatterDataBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .scatterdata import ScatterDataBlueprint

class DirectionDependentScatterDataBlueprint(ScatterDataBlueprint):
    """"""

    def __init__(self, name="DirectionDependentScatterData", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("sectors","sima/metocean/ScatterSector","",True,Dimension("*")))