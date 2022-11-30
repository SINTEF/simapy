# 
# Generated with FishNetBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .crosssection import CrossSectionBlueprint
from .crsaxialfrictionmodel import CRSAxialFrictionModelBlueprint

class FishNetBlueprint(CrossSectionBlueprint,CRSAxialFrictionModelBlueprint):
    """"""

    def __init__(self, name="FishNet", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("staticFriction","number","Static friction force corresponding to elongation",default=0.0))
        self.add_attribute(Attribute("staticElongation","number","Relative elongation",default=0.0))
        self.add_attribute(Attribute("dynamicFriction","number","Dynamic friction force corresponding to elongation",default=0.0))
        self.add_attribute(Attribute("dynamicElongation","number","Relative elongation",default=0.0))
        self.add_attribute(Attribute("axialFriction","boolean","Local axial friction model",default=False))
        self.add_attribute(Attribute("massDampingSpecification","boolean","Mass proportional Rayleigh damping",default=False))
        self.add_attribute(Attribute("stiffnessDampingSpecification","boolean","Stiffness proportional Rayleigh damping",default=False))
        self.add_attribute(Attribute("axialDampingSpecification","boolean","Local axial damping model",default=False))
        self.add_attribute(Attribute("temperature","number","Temperature at which the specification applies",default=0.0))
        self.add_attribute(Attribute("mass","number","Mass / unit length",default=0.0))
        self.add_attribute(Attribute("externalVolume","number","External volume per length",default=0.0))
        self.add_attribute(EnumAttribute("axialStiffnessInput","sima/riflex/AxialStiffness","Axial stiffness input specification"))
        self.add_attribute(Attribute("axialStiffness","number","Axial stiffness",default=0.0))
        self.add_attribute(BlueprintAttribute("axialStiffnessCharacteristics","sima/riflex/AxialStiffnessItem","",True,Dimension("*")))
        self.add_attribute(Attribute("solidityRatio","number","Solidity ratio.",default=0.0))
        self.add_attribute(Attribute("netWidthEnd1","number","Net width at segment end 1",default=0.0))
        self.add_attribute(Attribute("netWidthEnd2","number","Net width at segment end 2",default=0.0))
        self.add_attribute(Attribute("currentVelocityReduction","number","Reduction factor for current velocity.",default=1.0))
        self.add_attribute(BlueprintAttribute("massDamping","sima/riflex/CRSMassDamping","",True))
        self.add_attribute(BlueprintAttribute("stiffnessDamping","sima/riflex/CRSStiffnessDamping","",True))
        self.add_attribute(BlueprintAttribute("axialDamping","sima/riflex/CRSAxialDamping","",True))
        self.add_attribute(Attribute("amx","number","Added mass per length, tangential direction",default=0.0))
        self.add_attribute(Attribute("amy","number","Added mass per length, normal direction",default=0.0))
        self.add_attribute(Attribute("tensionCapacity","number","Tension capacity",default=0.0))
        self.add_attribute(Attribute("maxCurvature","number","Maximum curvature",default=0.0))