# 
# Generated with SeafloorSpringContactBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .seafloorcontact import SeafloorContactBlueprint

class SeafloorSpringContactBlueprint(SeafloorContactBlueprint):
    """"""

    def __init__(self, name="SeafloorSpringContact", package_path="sima/riflex", description=""):
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
        self.add_attribute(Attribute("normalStiffness","number","Normal stiffness parameter for seafloor",default=0.0))
        self.add_attribute(Attribute("normalDamping","number","Normal seafloor damping",default=0.0))
        self.add_attribute(Attribute("applyLateralContactForces","boolean","Apply lateral contact forces at the external contact radius, giving a torsional moment",default=False))