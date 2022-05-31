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
        self.attributes.append(Attribute("normalStiffness","number","Normal stiffness parameter for seafloor",default=0.0))
        self.attributes.append(Attribute("normalDamping","number","Normal seafloor damping",default=0.0))
        self.attributes.append(Attribute("applyLateralContactForces","boolean","Apply lateral contact forces at the external contact radius, giving a torsional moment",default=False))