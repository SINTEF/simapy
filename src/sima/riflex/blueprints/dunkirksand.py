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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("requiredResolution","integer","Required resolution of soil reaction curves",default=50))
        self.attributes.append(Attribute("pvDamping","number","",default=0.0))
        self.attributes.append(Attribute("mtDamping","number","",default=0.0))
        self.attributes.append(Attribute("baseShearLoadDamping","number","",default=0.0))
        self.attributes.append(Attribute("baseMomentDamping","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("lateralDisplacementForce","sima/riflex/DunkirkSoilCoefficients","",True))
        self.attributes.append(BlueprintAttribute("inPlaneMomentRotation","sima/riflex/DunkirkSoilCoefficients","",True))
        self.attributes.append(BlueprintAttribute("baseShearLoad","sima/riflex/DunkirkSoilCoefficients","",True))
        self.attributes.append(BlueprintAttribute("baseMoment","sima/riflex/DunkirkSoilCoefficients","",True))