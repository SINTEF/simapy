# 
# Generated with HydrostaticStiffnessMatrixDataBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hydrostaticstiffnessdata import HydrostaticStiffnessDataBlueprint

class HydrostaticStiffnessMatrixDataBlueprint(HydrostaticStiffnessDataBlueprint):
    """"""

    def __init__(self, name="HydrostaticStiffnessMatrixData", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("matrix","sima/hydro/HydrostaticStiffnessMatrix","",True))
        self.add_attribute(BlueprintAttribute("reference","sima/sima/Position","",True))