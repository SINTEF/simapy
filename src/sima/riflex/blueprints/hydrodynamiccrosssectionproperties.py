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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("itemNumber","integer","Global segment number",default=0))
        self.add_attribute(BlueprintAttribute("excitationZoneProperty","sima/riflex/ExcitationZoneProperty","Excitation zone",False))
        self.add_attribute(BlueprintAttribute("addedMassCrossFlowProperty","sima/riflex/AddedMassProperty","Cross-flow added mass",False))
        self.add_attribute(BlueprintAttribute("excitationCoefficientCrossFlowProperty","sima/riflex/ExcitationCoefficientsProperty","Cross-flow excitation coefficients",False))
        self.add_attribute(BlueprintAttribute("dampingFactorProperty","sima/riflex/DampingFactorProperty","Hydrodynamic damping factor",False))
        self.add_attribute(BlueprintAttribute("addedMassInLineProperty","sima/riflex/AddedMassProperty","In-line added mass",False))
        self.add_attribute(BlueprintAttribute("excitationCoefficientInLineProperty","sima/riflex/ExcitationCoefficientsProperty","In-line excitation coefficients",False))
        self.add_attribute(BlueprintAttribute("strouhalSpecificationProperty","sima/riflex/StrouhalSpecificationProperty","Strouhal number",False))