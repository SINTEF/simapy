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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("masterLine","sima/riflex/ARLine","Identification of master pipe.",False))
        self.attributes.append(BlueprintAttribute("slaveLine","sima/riflex/ARLine","Identification of slave pipe.",False))
        self.attributes.append(Attribute("firstMasterSegment","integer","First local segment in line for master pipe.",default=0))
        self.attributes.append(Attribute("lastMasterSegment","integer","Last local segment in line for master pipe.",default=0))
        self.attributes.append(Attribute("firstSlaveSegment","integer","First local segment in line for slave pipe.",default=0))
        self.attributes.append(Attribute("lastSlaveSegment","integer","Last local segment in line for slave pipe.",default=0))
        self.attributes.append(EnumAttribute("masterPipePosition","sima/riflex/InnerOuter","Position of master pipe."))
        self.attributes.append(EnumAttribute("stiffnessType","sima/riflex/StiffnessType","Stiffness code for contact force."))
        self.attributes.append(Attribute("relativeDamping","number","Desired relative damping level at estimated eigen period in the\npipe, pipe and contact spring system.",default=0.0))
        self.attributes.append(Attribute("damping","number","Dash pot damping coefficient per unit length of master pipe",default=0.0))
        self.attributes.append(Attribute("frictionStiffness","number","Spring stiffness associated with static friction coefficient",default=0.0))
        self.attributes.append(Attribute("staticFriction","number","Static friction coefficient.",default=0.0))
        self.attributes.append(Attribute("dynamicFriction","number","Dynamic (sliding) friction coefficient.",default=0.0))
        self.attributes.append(Attribute("axialFrictionEnabled","boolean","Axial (sliding) friction enabled.",default=False))
        self.attributes.append(Attribute("rotationalFrictionEnabled","boolean","Rotational (sliding) friction enabled.",default=False))
        self.attributes.append(Attribute("velocityLimitFriction","number","Velocity limit to change from sliding status (dynamic friction) to static\ndisplacement status (static friction)",default=0.0))
        self.attributes.append(Attribute("linearStiffness","number","Spring compression stiffness per unit length",default=0.0))
        self.attributes.append(BlueprintAttribute("stiffnessCharacteristics","sima/riflex/ContactSpringStiffnessItem","",True,Dimension("*")))
        self.attributes.append(Attribute("masterAsMainRiser","boolean","",default=False))
        self.attributes.append(Attribute("slaveAsMainRiser","boolean","",default=False))
        self.attributes.append(BlueprintAttribute("masterMainRiser","sima/riflex/MainRiserLine","Identification of master main riser",False))
        self.attributes.append(BlueprintAttribute("slaveMainRiser","sima/riflex/MainRiserLine","Identification of slave main riser",False))
        self.attributes.append(EnumAttribute("innerPipeLoading","sima/riflex/InnerPipeLoading",""))