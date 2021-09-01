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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("boundaryChangeOption","sima/riflex/BoundaryChangeOption","Boundary change option"))
        self.attributes.append(EnumAttribute("surgeConstraint","sima/riflex/BoundaryCondition","Boundary condition for translation in X-direction."))
        self.attributes.append(EnumAttribute("swayConstraint","sima/riflex/BoundaryCondition","Boundary condition for translation in Y-direction."))
        self.attributes.append(EnumAttribute("heaveConstraint","sima/riflex/BoundaryCondition","Boundary condition for translation in Z-direction."))
        self.attributes.append(EnumAttribute("rollConstraint","sima/riflex/BoundaryCondition","Boundary condition for rotation about X-axis"))
        self.attributes.append(EnumAttribute("pitchConstraint","sima/riflex/BoundaryCondition","Boundary condition for rotation about Y-axis"))
        self.attributes.append(EnumAttribute("yawConstraint","sima/riflex/BoundaryCondition","Boundary condition for rotation about Z-axis"))
        self.attributes.append(BlueprintAttribute("supportVessel","sima/riflex/SupportVessel","",False))
        self.attributes.append(EnumAttribute("_type","sima/riflex/BoundaryChangeReference",""))
        self.attributes.append(BlueprintAttribute("superNode","sima/simo/SuperNodeReference","",False))
        self.attributes.append(BlueprintAttribute("node","sima/riflex/NodeReference","",True))
        self.attributes.append(EnumAttribute("masterType","sima/riflex/BoundaryChangeReference",""))
        self.attributes.append(BlueprintAttribute("master","sima/simo/SuperNodeReference","",False))
        self.attributes.append(BlueprintAttribute("masterNodeReference","sima/riflex/NodeReference","",True))