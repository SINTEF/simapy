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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("axialStiffness","number","Horizontal stiffness parameter for seafloor in axial direction",default=0.0))
        self.add_attribute(Attribute("axialFriction","number","Horizontal friction parameter for seafloor in axial direction",default=0.0))
        self.add_attribute(Attribute("axialDamping","number","Axial seafloor damping ",default=0.0))
        self.add_attribute(Attribute("lateralStiffness","number","Horizontal stiffness parameter for seafloor in lateral direction",default=0.0))
        self.add_attribute(Attribute("lateralFriction","number","Horizontal stiffness parameter for seafloor in lateral direction",default=0.0))
        self.add_attribute(Attribute("lateralDamping","number","Lateral seafloor damping",default=0.0))
        self.add_attribute(Attribute("soilSubmergedWeight","number","Soil submerged weight",default=0.0))
        self.add_attribute(Attribute("soilShearStrength","number"," Soil shear strength at seabed",default=0.0))
        self.add_attribute(Attribute("soilShearStrengthGradient","number","Soil shear strength vertical gradient",default=0.0))
        self.add_attribute(Attribute("soilPoissonRatio","number","Soil Poisson ratio",default=0.0))
        self.add_attribute(Attribute("soilGModulus","number","Soil G-modulus/compressive strength",default=0.0))
        self.add_attribute(Attribute("stiffnessModulusRelationship","number","Relationship between dynamic stiffness and G-modulus",default=0.88))
        self.add_attribute(Attribute("alpha","number","Scaling factor for peak soil suction relative to peak soil compression",default=1.0))
        self.add_attribute(Attribute("beta","number","Scaling factor for peak soil suction relative to peak soil compression",default=1.0))
        self.add_attribute(Attribute("kbc","number","Mobilization displacement for soil bearing capacity as fraction of pipe soil contact width",default=0.05))
        self.add_attribute(Attribute("kt","number","Mobilization displacement for max soil suction as fraction of pipe soil contact width",default=0.08))