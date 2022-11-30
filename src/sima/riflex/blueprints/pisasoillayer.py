# 
# Generated with PisaSoilLayerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class PisaSoilLayerBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="PisaSoilLayer", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("soilType","sima/riflex/SoilType","",False))
        self.add_attribute(Attribute("deltaZ","number","Height of soil layer",default=0.0))
        self.add_attribute(Attribute("shearModulusTop","number","Shear modulus at top of soil layer",default=0.0))
        self.add_attribute(Attribute("shearModulusBottom","number","Shear modulus at bottom of soil layer",default=0.0))
        self.add_attribute(Attribute("effectiveWeightTop","number","Effective soil weight (gamma) at top of soil layer",default=0.0))
        self.add_attribute(Attribute("effectiveWeightBottom","number","Effective soil weight (gamma) at bottom of soil layer",default=0.0))
        self.add_attribute(Attribute("undrainedShearStrengthTop","number","Undrained shear strength (Su) at top of soil layer. Applies for clay only.",default=0.0))
        self.add_attribute(Attribute("undrainedShearStrengthBottom","number","Undrained shear strength (Su) at bottom of soil layer. Applies for clay only.",default=0.0))
        self.add_attribute(Attribute("relativeDensity","number","Relative density used for scaling soil curve. Applies for Dunkirk sand only.",default=100.0))