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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("staticFriction","number","Static friction force corresponding to elongation",default=0.0))
        self.attributes.append(Attribute("staticElongation","number","Relative elongation",default=0.0))
        self.attributes.append(Attribute("dynamicFriction","number","Dynamic friction force corresponding to elongation",default=0.0))
        self.attributes.append(Attribute("dynamicElongation","number","Relative elongation",default=0.0))
        self.attributes.append(Attribute("axialFriction","boolean","Local axial friction model",default=False))
        self.attributes.append(Attribute("massDampingSpecification","boolean","Mass proportional Rayleigh damping",default=False))
        self.attributes.append(Attribute("stiffnessDampingSpecification","boolean","Stiffness proportional Rayleigh damping",default=False))
        self.attributes.append(Attribute("axialDampingSpecification","boolean","Local axial damping model",default=False))
        self.attributes.append(Attribute("temperature","number","Temperature at which the specification applies",default=0.0))
        self.attributes.append(Attribute("mass","number","Mass / unit length",default=0.0))
        self.attributes.append(Attribute("externalVolume","number","External volume per length",default=0.0))
        self.attributes.append(EnumAttribute("axialStiffnessInput","sima/riflex/AxialStiffness","Axial stiffness input specification"))
        self.attributes.append(Attribute("axialStiffness","number","Axial stiffness",default=0.0))
        self.attributes.append(BlueprintAttribute("axialStiffnessCharacteristics","sima/riflex/AxialStiffnessItem","",True,Dimension("*")))
        self.attributes.append(Attribute("solidityRatio","number","Solidity ratio.",default=0.0))
        self.attributes.append(Attribute("netWidthEnd1","number","Net width at segment end 1",default=0.0))
        self.attributes.append(Attribute("netWidthEnd2","number","Net width at segment end 2",default=0.0))
        self.attributes.append(Attribute("currentVelocityReduction","number","Reduction factor for current velocity.",default=1.0))
        self.attributes.append(BlueprintAttribute("massDamping","sima/riflex/CRSMassDamping","",True))
        self.attributes.append(BlueprintAttribute("stiffnessDamping","sima/riflex/CRSStiffnessDamping","",True))
        self.attributes.append(BlueprintAttribute("axialDamping","sima/riflex/CRSAxialDamping","",True))
        self.attributes.append(Attribute("amx","number","Added mass per length, tangential direction",default=0.0))
        self.attributes.append(Attribute("amy","number","Added mass per length, normal direction",default=0.0))
        self.attributes.append(Attribute("tensionCapacity","number","Tension capacity",default=0.0))
        self.attributes.append(Attribute("maxCurvature","number","Maximum curvature",default=0.0))