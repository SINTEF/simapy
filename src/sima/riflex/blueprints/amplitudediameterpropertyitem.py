# 
# Generated with AmplitudeDiameterPropertyItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class AmplitudeDiameterPropertyItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="AmplitudeDiameterPropertyItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("nonDimensionalFrequency","number","Non-dimensional frequency",default=0.0))
        self.add_attribute(Attribute("adRatioCl0","number","A/D ratio when CL = 0",default=0.0))
        self.add_attribute(Attribute("adRatioClMax","number","A/D ratio when CL = CLMax",default=0.0))
        self.add_attribute(Attribute("maxExcitationCoefficient","number","Maximum excitation coefficient",default=0.0))
        self.add_attribute(Attribute("excitCoeffAd0","number","Excitation coefficient for A/D=0",default=0.0))