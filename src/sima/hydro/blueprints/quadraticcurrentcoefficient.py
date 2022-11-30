# 
# Generated with QuadraticCurrentCoefficientBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class QuadraticCurrentCoefficientBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="QuadraticCurrentCoefficient", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("symmetry","sima/hydro/DirectionSymmetry",""))
        self.add_attribute(BlueprintAttribute("items","sima/hydro/QuadraticCurrentCoefficientItem","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("_type","sima/hydro/CoefficientType","Current coefficient type"))
        self.add_attribute(Attribute("fileName","string","Text file containing the current coefficients. The force coefficents in the file must be specified in [kN/(m/s)] for translational degrees of freedom and [kN.s] for rotational degrees of freedom."))