# 
# Generated with LinearCurrentCoefficientItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class LinearCurrentCoefficientItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="LinearCurrentCoefficientItem", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("direction","number","Direction",default=0.0))
        self.add_attribute(Attribute("c11","number","Linear current force coefficient for 1. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c12","number","Linear current force coefficient for 2. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c13","number","Linear current force coefficient for 3. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c14","number","Linear current force coefficient for 4. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c15","number","Linear current force coefficient for 5. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c16","number","Linear current force coefficient for 6. degree of freedom",default=0.0))