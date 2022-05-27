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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("direction","number","Direction",default=0.0))
        self.attributes.append(Attribute("c21","number","Quadratic current force coefficient for 1. degree of freedom",default=0.0))
        self.attributes.append(Attribute("c22","number","Quadratic current force coefficient for 2. degree of freedom",default=0.0))
        self.attributes.append(Attribute("c23","number","Quadratic current force coefficient for 3. degree of freedom",default=0.0))
        self.attributes.append(Attribute("c24","number","Quadratic current force coefficient for 4. degree of freedom",default=0.0))
        self.attributes.append(Attribute("c25","number","Quadratic current force coefficient for 5. degree of freedom",default=0.0))
        self.attributes.append(Attribute("c26","number","Quadratic current force coefficient for 6. degree of freedom",default=0.0))