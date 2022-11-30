# 
# Generated with QuadraticWindCoefficientBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class QuadraticWindCoefficientBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="QuadraticWindCoefficient", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("symmetry","sima/hydro/DirectionSymmetry",""))
        self.add_attribute(Attribute("windArea","number","",default=2000.0))
        self.add_attribute(Attribute("referenceHeight","number","Reference height for wind velocity",default=10.0))
        self.add_attribute(BlueprintAttribute("items","sima/hydro/QuadraticWindCoefficientItem","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("_type","sima/hydro/CoefficientType","Wind coefficient type"))
        self.add_attribute(Attribute("fileName","string","Text file containing the wind coefficients. The force coefficents in the file must be specified in [kN/(m/s)] for translational degrees of freedom and [kN.s] for rotational degrees of freedom."))