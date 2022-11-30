# 
# Generated with QuadraticWindCoefficientItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class QuadraticWindCoefficientItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="QuadraticWindCoefficientItem", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("direction","number","Direction",default=0.0))
        self.add_attribute(Attribute("c1","number","Wind force coefficient for 1. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c2","number","Wind force coefficient for 2. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c3","number","Wind force coefficient for 3. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c4","number","Wind force coefficient for 4. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c5","number","Wind force coefficient for 5. degree of freedom",default=0.0))
        self.add_attribute(Attribute("c6","number","Wind force coefficient for 6. degree of freedom",default=0.0))