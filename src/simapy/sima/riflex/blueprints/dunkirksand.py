# 
# Generated with DunkirkSandBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .dunkirksoiltype import DunkirkSoilTypeBlueprint

class DunkirkSandBlueprint(DunkirkSoilTypeBlueprint):
    """"""

    def __init__(self, name="DunkirkSand", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("requiredResolution","integer","Required resolution of soil reaction curves",default=50))
        self.add_attribute(Attribute("pvDamping","number","",default=0.0))
        self.add_attribute(Attribute("mtDamping","number","",default=0.0))
        self.add_attribute(Attribute("baseShearLoadDamping","number","",default=0.0))
        self.add_attribute(Attribute("baseMomentDamping","number","",default=0.0))
        self.add_attribute(BlueprintAttribute("lateralDisplacementForce","sima/riflex/DunkirkSoilCoefficients","",True))
        self.add_attribute(BlueprintAttribute("inPlaneMomentRotation","sima/riflex/DunkirkSoilCoefficients","",True))
        self.add_attribute(BlueprintAttribute("baseShearLoad","sima/riflex/DunkirkSoilCoefficients","",True))
        self.add_attribute(BlueprintAttribute("baseMoment","sima/riflex/DunkirkSoilCoefficients","",True))