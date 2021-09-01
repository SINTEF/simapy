# 
# Generated with DepthDependenthydrodynamicCoefficientBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DepthDependenthydrodynamicCoefficientBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DepthDependenthydrodynamicCoefficient", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("zd","number","Vertical position",default=1.0))
        self.attributes.append(Attribute("rvol","number","Volume relative to fully submerged volume",default=1.0))
        self.attributes.append(Attribute("ramx","number","Relative added mass in 1. degree of freedom",default=1.0))
        self.attributes.append(Attribute("ramy","number","Relative added mass in 2. degree of freedom",default=1.0))
        self.attributes.append(Attribute("ramz","number","Relative added mass in 3. degree of freedom",default=1.0))
        self.attributes.append(Attribute("rc11","number","Relative linear drag in 1. degree of freedom",default=0.0))
        self.attributes.append(Attribute("rc12","number","Relative linear drag in 2. degree of freedom",default=0.0))
        self.attributes.append(Attribute("rc13","number","Relative linear drag in 3. degree of freedom",default=0.0))
        self.attributes.append(Attribute("rc21","number","Relative quadratic drag in 1. degree of freedom",default=0.0))
        self.attributes.append(Attribute("rc22","number","Relative quadrativ drag in 2. degree of freedom",default=0.0))
        self.attributes.append(Attribute("rc23","number","Relative quadratic drag in 3. degree of freedom",default=0.0))