# 
# Generated with NodeBoundaryChangeItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class NodeBoundaryChangeItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="NodeBoundaryChangeItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("boundaryChangeOption","sima/riflex/BoundaryChangeOption","Boundary change option"))
        self.add_attribute(EnumAttribute("surgeConstraint","sima/riflex/BoundaryCondition","Boundary condition for translation in X-direction."))
        self.add_attribute(EnumAttribute("swayConstraint","sima/riflex/BoundaryCondition","Boundary condition for translation in Y-direction."))
        self.add_attribute(EnumAttribute("heaveConstraint","sima/riflex/BoundaryCondition","Boundary condition for translation in Z-direction."))
        self.add_attribute(EnumAttribute("rollConstraint","sima/riflex/BoundaryCondition","Boundary condition for rotation about X-axis"))
        self.add_attribute(EnumAttribute("pitchConstraint","sima/riflex/BoundaryCondition","Boundary condition for rotation about Y-axis"))
        self.add_attribute(EnumAttribute("yawConstraint","sima/riflex/BoundaryCondition","Boundary condition for rotation about Z-axis"))
        self.add_attribute(BlueprintAttribute("supportVessel","sima/riflex/SupportVessel","",False))
        self.add_attribute(EnumAttribute("_type","sima/riflex/BoundaryChangeReference",""))
        self.add_attribute(BlueprintAttribute("superNode","sima/simo/SuperNodeReference","",False))
        self.add_attribute(BlueprintAttribute("node","sima/riflex/NodeReference","",True))
        self.add_attribute(EnumAttribute("masterType","sima/riflex/BoundaryChangeReference",""))
        self.add_attribute(BlueprintAttribute("master","sima/simo/SuperNodeReference","",False))
        self.add_attribute(BlueprintAttribute("masterNodeReference","sima/riflex/NodeReference","",True))