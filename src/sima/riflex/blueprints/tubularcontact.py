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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("radius","number","Contact radius",default=0.0))
        self.add_attribute(EnumAttribute("direction","sima/riflex/ContactDirection","Contact direction."))
        self.add_attribute(Attribute("constantStiffness","boolean","Stiffness code for contact force.",default=False))
        self.add_attribute(Attribute("desiredDamping","number","Desired relative damping level at estimated eigen period in the pipe and contact spring system.",default=0.0))
        self.add_attribute(Attribute("dampingCoefficient","number","Dash pot damping coefficient",default=0.0))
        self.add_attribute(Attribute("stiffness","number","Spring stiffness associated with static friction coefficient",default=0.0))
        self.add_attribute(Attribute("staticFriction","number","Static friction coefficient.",default=0.0))
        self.add_attribute(Attribute("dynamicFriction","number","Dynamic (sliding) friction coefficient.",default=0.0))
        self.add_attribute(EnumAttribute("slidingFriction","sima/riflex/ControlParameter","Control parameter for axial sliding friction."))
        self.add_attribute(EnumAttribute("rotationFriction","sima/riflex/ControlParameter","Control parameter for friction caused by rotation."))
        self.add_attribute(Attribute("velocityLimit","number","Velocity limit to change from sliding status (dynamic friction) to static displacement status (static friction)",default=0.0))
        self.add_attribute(Attribute("compressionStiffness","number","Spring compression stiffness",default=0.0))
        self.add_attribute(BlueprintAttribute("stiffnessItems","sima/riflex/SpringStiffnessItem","",True,Dimension("*")))