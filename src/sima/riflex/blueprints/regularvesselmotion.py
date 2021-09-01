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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("supportVessel","sima/riflex/SupportVessel","",False))
        self.attributes.append(Attribute("amplitudeX","number","Motion amplitude, x-direction",default=0.0))
        self.attributes.append(Attribute("amplitudeY","number","Motion amplitude, y-direction",default=0.0))
        self.attributes.append(Attribute("amplitudeZ","number","Motion amplitude, z-direction",default=0.0))
        self.attributes.append(Attribute("amplitudeXR","number","Motion amplitude, x-rotation",default=0.0))
        self.attributes.append(Attribute("amplitudeYR","number","Motion amplitude, y-rotation",default=0.0))
        self.attributes.append(Attribute("amplitudeZR","number","Motion amplitude, z-rotation",default=0.0))
        self.attributes.append(Attribute("period","number","Period of motion",default=0.0))
        self.attributes.append(Attribute("phaseX","number","Phase angle, x-motion",default=0.0))
        self.attributes.append(Attribute("phaseY","number","Phase angle, y-motion",default=0.0))
        self.attributes.append(Attribute("phaseZ","number","Phase angle, z-motion",default=0.0))
        self.attributes.append(Attribute("phaseXR","number","Phase angle, x-rotation",default=0.0))
        self.attributes.append(Attribute("phaseYR","number","Phase angle, y-rotation",default=0.0))
        self.attributes.append(Attribute("phaseZR","number","Phase angle, z-rotation",default=0.0))