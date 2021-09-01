# 
# Generated with TubularContactBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class TubularContactBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="TubularContact", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("radius","number","Contact radius",default=0.0))
        self.attributes.append(EnumAttribute("direction","sima/riflex/ContactDirection","Contact direction."))
        self.attributes.append(Attribute("constantStiffness","boolean","Stiffness code for contact force.",default=False))
        self.attributes.append(Attribute("desiredDamping","number","Desired relative damping level at estimated eigen period in the pipe and contact spring system.",default=0.0))
        self.attributes.append(Attribute("dampingCoefficient","number","Dash pot damping coefficient",default=0.0))
        self.attributes.append(Attribute("stiffness","number","Spring stiffness associated with static friction coefficient",default=0.0))
        self.attributes.append(Attribute("staticFriction","number","Static friction coefficient.",default=0.0))
        self.attributes.append(Attribute("dynamicFriction","number","Dynamic (sliding) friction coefficient.",default=0.0))
        self.attributes.append(EnumAttribute("slidingFriction","sima/riflex/ControlParameter","Control parameter for axial sliding friction."))
        self.attributes.append(EnumAttribute("rotationFriction","sima/riflex/ControlParameter","Control parameter for friction caused by rotation."))
        self.attributes.append(Attribute("velocityLimit","number","Velocity limit to change from sliding status (dynamic friction) to static displacement status (static friction)",default=0.0))
        self.attributes.append(Attribute("compressionStiffness","number","Spring compression stiffness",default=0.0))
        self.attributes.append(BlueprintAttribute("stiffnessItems","sima/riflex/SpringStiffnessItem","",True,Dimension("size","")))