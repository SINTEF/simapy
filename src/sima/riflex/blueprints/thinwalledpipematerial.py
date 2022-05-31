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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("materialModel","sima/riflex/MaterialModel","Type of material model."))
        self.attributes.append(Attribute("elasticityModulus","number","Modulus of elasticity",default=0.0))
        self.attributes.append(Attribute("shearModulus","number","Shear modulus",default=0.0))
        self.attributes.append(Attribute("yieldStress","number","Yield stress",default=0.0))
        self.attributes.append(Attribute("strainStressCurveRise","number","Rise of strain-stress curve for plastic region.",default=0.0))
        self.attributes.append(Attribute("materialHardening","number","Hardening parameter for material.",default=1.0))
        self.attributes.append(Attribute("numIntegrationPoints","integer","Number of integration points along circumference.",default=16))
        self.attributes.append(BlueprintAttribute("strainStressCharacteristics","sima/riflex/StrainStressItem","Strain-stress curve.",True,Dimension("*")))