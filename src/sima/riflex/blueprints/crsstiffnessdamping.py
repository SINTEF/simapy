# 
# Generated with CRSStiffnessDampingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class CRSStiffnessDampingBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CRSStiffnessDamping", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("axialFactor","number","Factor for stiffness proportional damping in axial dof",default=0.0))
        self.add_attribute(Attribute("torsionalFactor","number","Factor for stiffness proportional damping in torsional dof",default=0.0))
        self.add_attribute(Attribute("bendingFactor","number","Factor for stiffness proportional damping in bending dof",default=0.0))
        self.add_attribute(EnumAttribute("option","sima/riflex/RayleighDamping","Stiffness proportional damping options"))