# 
# Generated with LinearCurrentCoefficientBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class LinearCurrentCoefficientBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="LinearCurrentCoefficient", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("symmetry","sima/hydro/DirectionSymmetry",""))
        self.attributes.append(BlueprintAttribute("items","sima/hydro/LinearCurrentCoefficientItem","",True,Dimension("*")))