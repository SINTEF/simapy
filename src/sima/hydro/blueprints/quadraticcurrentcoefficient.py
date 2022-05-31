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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("symmetry","sima/hydro/DirectionSymmetry",""))
        self.attributes.append(BlueprintAttribute("items","sima/hydro/QuadraticCurrentCoefficientItem","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("_type","sima/hydro/CoefficientType","Current coefficient type"))
        self.attributes.append(Attribute("fileName","string","Text file containing the current coefficients. The force coefficents in the file must be specified in [kN/(m/s)] for translational degrees of freedom and [kN.s] for rotational degrees of freedom.",default=""))