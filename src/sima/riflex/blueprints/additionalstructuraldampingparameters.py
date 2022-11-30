# 
# Generated with AdditionalStructuralDampingParametersBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class AdditionalStructuralDampingParametersBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="AdditionalStructuralDampingParameters", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("globalSegmentNumber","integer","Global segment number",default=0))
        self.add_attribute(Attribute("structuralDampingFile","string","File with detailed structural damping specification, see VIVANA user manual"))