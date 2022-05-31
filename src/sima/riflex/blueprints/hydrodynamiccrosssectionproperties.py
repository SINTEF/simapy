# 
# Generated with HydrodynamicCrossSectionPropertiesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class HydrodynamicCrossSectionPropertiesBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="HydrodynamicCrossSectionProperties", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("itemNumber","integer","Global segment number",default=0))
        self.attributes.append(BlueprintAttribute("excitationZoneProperty","sima/riflex/ExcitationZoneProperty","Excitation zone",False))
        self.attributes.append(BlueprintAttribute("addedMassCrossFlowProperty","sima/riflex/AddedMassProperty","Cross-flow added mass",False))
        self.attributes.append(BlueprintAttribute("excitationCoefficientCrossFlowProperty","sima/riflex/ExcitationCoefficientsProperty","Cross-flow excitation coefficients",False))
        self.attributes.append(BlueprintAttribute("dampingFactorProperty","sima/riflex/DampingFactorProperty","Hydrodynamic damping factor",False))
        self.attributes.append(BlueprintAttribute("addedMassInLineProperty","sima/riflex/AddedMassProperty","In-line added mass",False))
        self.attributes.append(BlueprintAttribute("excitationCoefficientInLineProperty","sima/riflex/ExcitationCoefficientsProperty","In-line excitation coefficients",False))
        self.attributes.append(BlueprintAttribute("strouhalSpecificationProperty","sima/riflex/StrouhalSpecificationProperty","Strouhal number",False))