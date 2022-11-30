# 
# Generated with AmplitudeDiameterExcitationCoefficientItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class AmplitudeDiameterExcitationCoefficientItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="AmplitudeDiameterExcitationCoefficientItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("amplitudeDiameterRatio","number","Amplitude to diameter ratio",default=0.0))
        self.add_attribute(Attribute("excitationCoefficient","number","Excitation coefficient",default=0.0))