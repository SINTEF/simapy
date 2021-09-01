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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("soilType","sima/riflex/SoilType","",False))
        self.attributes.append(Attribute("deltaZ","number","Height of soil layer",default=0.0))
        self.attributes.append(Attribute("shearModulusTop","number","Shear modulus at top of soil layer",default=0.0))
        self.attributes.append(Attribute("shearModulusBottom","number","Shear modulus at bottom of soil layer",default=0.0))
        self.attributes.append(Attribute("effectiveWeightTop","number","Effective soil weight (gamma) at top of soil layer",default=0.0))
        self.attributes.append(Attribute("effectiveWeightBottom","number","Effective soil weight (gamma) at bottom of soil layer",default=0.0))
        self.attributes.append(Attribute("undrainedShearStrengthTop","number","Undrained shear strength (Su) at top of soil layer. Applies for clay only.",default=0.0))
        self.attributes.append(Attribute("undrainedShearStrengthBottom","number","Undrained shear strength (Su) at bottom of soil layer. Applies for clay only.",default=0.0))
        self.attributes.append(Attribute("relativeDensity","number","Relative density used for scaling soil curve. Applies for Dunkirk sand only.",default=100.0))