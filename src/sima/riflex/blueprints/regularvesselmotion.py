# 
# Generated with RegularVesselMotionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class RegularVesselMotionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RegularVesselMotion", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("supportVessel","sima/riflex/SupportVessel","",False))
        self.add_attribute(Attribute("amplitudeX","number","Motion amplitude, x-direction",default=0.0))
        self.add_attribute(Attribute("amplitudeY","number","Motion amplitude, y-direction",default=0.0))
        self.add_attribute(Attribute("amplitudeZ","number","Motion amplitude, z-direction",default=0.0))
        self.add_attribute(Attribute("amplitudeXR","number","Motion amplitude, x-rotation",default=0.0))
        self.add_attribute(Attribute("amplitudeYR","number","Motion amplitude, y-rotation",default=0.0))
        self.add_attribute(Attribute("amplitudeZR","number","Motion amplitude, z-rotation",default=0.0))
        self.add_attribute(Attribute("period","number","Period of motion",default=0.0))
        self.add_attribute(Attribute("phaseX","number","Phase angle, x-motion",default=0.0))
        self.add_attribute(Attribute("phaseY","number","Phase angle, y-motion",default=0.0))
        self.add_attribute(Attribute("phaseZ","number","Phase angle, z-motion",default=0.0))
        self.add_attribute(Attribute("phaseXR","number","Phase angle, x-rotation",default=0.0))
        self.add_attribute(Attribute("phaseYR","number","Phase angle, y-rotation",default=0.0))
        self.add_attribute(Attribute("phaseZR","number","Phase angle, z-rotation",default=0.0))