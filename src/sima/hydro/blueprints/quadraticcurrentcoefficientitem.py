# 
# Generated with QuadraticCurrentCoefficientItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class QuadraticCurrentCoefficientItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="QuadraticCurrentCoefficientItem", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("direction","number","Direction",default=0.0))
        self.add_attribute(Attribute("c21","number","Quadratic current force coefficient for 1. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c22","number","Quadratic current force coefficient for 2. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c23","number","Quadratic current force coefficient for 3. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c24","number","Quadratic current force coefficient for 4. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c25","number","Quadratic current force coefficient for 5. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c26","number","Quadratic current force coefficient for 6. degree of freedom",default=0.0))