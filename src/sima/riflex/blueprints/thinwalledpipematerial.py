# 
# Generated with ThinWalledPipeMaterialBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ThinWalledPipeMaterialBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ThinWalledPipeMaterial", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("materialModel","sima/riflex/MaterialModel","Type of material model."))
        self.add_attribute(Attribute("elasticityModulus","number","Modulus of elasticity",default=0.0))
        self.add_attribute(Attribute("shearModulus","number","Shear modulus",default=0.0))
        self.add_attribute(Attribute("yieldStress","number","Yield stress",default=0.0))
        self.add_attribute(Attribute("strainStressCurveRise","number","Rise of strain-stress curve for plastic region.",default=0.0))
        self.add_attribute(Attribute("materialHardening","number","Hardening parameter for material.",default=1.0))
        self.add_attribute(Attribute("numIntegrationPoints","integer","Number of integration points along circumference.",default=16))
        self.add_attribute(BlueprintAttribute("strainStressCharacteristics","sima/riflex/StrainStressItem","Strain-stress curve.",True,Dimension("*")))