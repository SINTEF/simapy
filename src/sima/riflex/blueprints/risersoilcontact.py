# 
# Generated with RiserSoilContactBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .seafloorcontact import SeafloorContactBlueprint

class RiserSoilContactBlueprint(SeafloorContactBlueprint):
    """"""

    def __init__(self, name="RiserSoilContact", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("axialStiffness","number","Horizontal stiffness parameter for seafloor in axial direction",default=0.0))
        self.attributes.append(Attribute("axialFriction","number","Horizontal friction parameter for seafloor in axial direction",default=0.0))
        self.attributes.append(Attribute("axialDamping","number","Axial seafloor damping ",default=0.0))
        self.attributes.append(Attribute("lateralStiffness","number","Horizontal stiffness parameter for seafloor in lateral direction",default=0.0))
        self.attributes.append(Attribute("lateralFriction","number","Horizontal stiffness parameter for seafloor in lateral direction",default=0.0))
        self.attributes.append(Attribute("lateralDamping","number","Lateral seafloor damping",default=0.0))
        self.attributes.append(Attribute("soilSubmergedWeight","number","Soil submerged weight",default=0.0))
        self.attributes.append(Attribute("soilShearStrength","number"," Soil shear strength at seabed",default=0.0))
        self.attributes.append(Attribute("soilShearStrengthGradient","number","Soil shear strength vertical gradient",default=0.0))
        self.attributes.append(Attribute("soilPoissonRatio","number","Soil Poisson ratio",default=0.0))
        self.attributes.append(Attribute("soilGModulus","number","Soil G-modulus/compressive strength",default=0.0))
        self.attributes.append(Attribute("stiffnessModulusRelationship","number","Relationship between dynamic stiffness and G-modulus",default=0.88))
        self.attributes.append(Attribute("alpha","number","Scaling factor for peak soil suction relative to peak soil compression",default=1.0))
        self.attributes.append(Attribute("beta","number","Scaling factor for peak soil suction relative to peak soil compression",default=1.0))
        self.attributes.append(Attribute("kbc","number","Mobilization displacement for soil bearing capacity as fraction of pipe soil contact width",default=0.05))
        self.attributes.append(Attribute("kt","number","Mobilization displacement for max soil suction as fraction of pipe soil contact width",default=0.08))