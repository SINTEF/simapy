# 
# Generated with PipeInPipeContactBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class PipeInPipeContactBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="PipeInPipeContact", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("masterLine","sima/riflex/ARLine","Identification of master pipe.",False))
        self.add_attribute(BlueprintAttribute("slaveLine","sima/riflex/ARLine","Identification of slave pipe.",False))
        self.add_attribute(Attribute("firstMasterSegment","integer","First local segment in line for master pipe.",default=0))
        self.add_attribute(Attribute("lastMasterSegment","integer","Last local segment in line for master pipe.",default=0))
        self.add_attribute(Attribute("firstSlaveSegment","integer","First local segment in line for slave pipe.",default=0))
        self.add_attribute(Attribute("lastSlaveSegment","integer","Last local segment in line for slave pipe.",default=0))
        self.add_attribute(EnumAttribute("masterPipePosition","sima/riflex/InnerOuter","Position of master pipe."))
        self.add_attribute(EnumAttribute("stiffnessType","sima/riflex/StiffnessType","Stiffness code for contact force."))
        self.add_attribute(Attribute("relativeDamping","number","Desired relative damping level at estimated eigen period in the\npipe, pipe and contact spring system.",default=0.0))
        self.add_attribute(Attribute("damping","number","Dash pot damping coefficient per unit length of master pipe",default=0.0))
        self.add_attribute(Attribute("frictionStiffness","number","Spring stiffness associated with static friction coefficient",default=0.0))
        self.add_attribute(Attribute("staticFriction","number","Static friction coefficient.",default=0.0))
        self.add_attribute(Attribute("dynamicFriction","number","Dynamic (sliding) friction coefficient.",default=0.0))
        self.add_attribute(Attribute("axialFrictionEnabled","boolean","Axial (sliding) friction enabled.",default=False))
        self.add_attribute(Attribute("rotationalFrictionEnabled","boolean","Rotational (sliding) friction enabled.",default=False))
        self.add_attribute(Attribute("velocityLimitFriction","number","Velocity limit to change from sliding status (dynamic friction) to static\ndisplacement status (static friction)",default=0.0))
        self.add_attribute(Attribute("linearStiffness","number","Spring compression stiffness per unit length",default=0.0))
        self.add_attribute(BlueprintAttribute("stiffnessCharacteristics","sima/riflex/ContactSpringStiffnessItem","",True,Dimension("*")))
        self.add_attribute(Attribute("masterAsMainRiser","boolean","",default=False))
        self.add_attribute(Attribute("slaveAsMainRiser","boolean","",default=False))
        self.add_attribute(BlueprintAttribute("masterMainRiser","sima/riflex/MainRiserLine","Identification of master main riser",False))
        self.add_attribute(BlueprintAttribute("slaveMainRiser","sima/riflex/MainRiserLine","Identification of slave main riser",False))
        self.add_attribute(EnumAttribute("innerPipeLoading","sima/riflex/InnerPipeLoading",""))